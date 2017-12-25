//todo: add verify function,only varchar and numbers can be accepted
//todo: small hand when staying on the button
//todo: verify the authority
//todo: login and logup
//todo: add status control in tables and in codes
//todo: handle control and verify when server run error and return ""
//todo: big bug ---->how to support to change config and save
//todo: ---------> precisely location return html.segment location returned list
//todo: write blog to summarize mutiple data insert.
//todo: table name/js file name ....best practice :project_function_name
//todo: lock table when operate Model Setting.
//todo: django transaction http://www.cnblogs.com/znicy/p/5434829.html
// http://blog.csdn.net/qq_23934063/article/details/72809279
//todo: django exclude stands for !=
//todo: python deepcopy and copy;deepcopy is value copy.

class main{

    static handle_err(status){
        alert('AJAX ERROR CODE:'+status)
    }

    static rewrite_table_title(id,title){
        let ht = '';
        ht += '<thead><tr>';
        for(let t of title){
            ht += `<th>${t}</th>`
        }
        ht += '</tr></thead><tbody id="tbody"></tbody>';
        document.getElementById(id).innerHTML = ht
    }

    static display_two_buttons(location,func,args = ''){
        let brackets = '';
        args === ''? brackets = '()': brackets = `('${args}')`;
        let html = '';
        html = `
        <button type="button" class="btn btn-default">cancle</button>
        <button type="button" onclick="${func}${brackets}" class="btn btn-default">save</button>`;
        document.getElementById(location).innerHTML = html
    }

    static ajax(method,path,data='') {
        let request = new XMLHttpRequest();
        return new Promise((resolve,reject)=>{
            request.open(method,path);
            request.onreadystatechange = ()=>{
                if(request.readyState === 4){
                    request.status === 200 ? resolve(request.responseText) : reject(request.status);
                }
            };
            if(method === 'POST'){
                request.setRequestHeader('Content-type','application/json');
            }
            request.send(data);
        })
    }

    static make_table_rows(text,bodyId,rowFunc,rowFlag){
        let parsed = JSON.parse(text);
        let html = '';
        switch(rowFlag){
            case 'dict':
                for(let p of parsed.arr_dict){
                    html += rowFunc(p)
                }
                break;
            case 'list':
                for(let p of parsed.arr_arr){
                    html += rowFunc(p);
                }
                break;
        }
        document.getElementById(bodyId).innerHTML = html;
        return html
    }

    static load_table(path,ajaxMethod,titles,rowFunc,rowFlag='dict',bodyId='tbody',tableId='table_id',data='',otheFunc=undefined,otherArgs=''){
        let req = this.ajax(ajaxMethod,path);
        req.then((text)=>{
            this.rewrite_table_title(tableId,titles);
            this.make_table_rows(text,bodyId,rowFunc,rowFlag);
            if(otheFunc !== undefined){
                otheFunc(otherArgs);
            }
        }).catch((status)=>{
            this.handle_err(status);
        })
    }
}

class model_running extends main{
    static load_table(){
        let path = '/mobyheart/display-model-links/';
        let method = 'GET';
        let titles = ['Number','Model Name','Link','Status','Start','Stop'];
        super.load_table(path,method,titles,this.row_func);
    }
    static row_func(p){
        let trId = 'tr'+p.id;
        let html = `<tr id='${trId}'>
            <td>${p.id}</td>
            <td>${p.model_name}</td>
            <td>${p.created_link}</td>
            <td>${p.status}</td>
            <td>${p.start}</td>
            <td>${p.stop}</td>
         </tr>`;
        return html
    }
    //need to cover button
}

class model_setting extends main{

    static load_table(){
        let path = '/mobyheart/load-model-list/';
        let titles = ['Number','Model Name','Author'];
        document.getElementById("button_id").innerHTML = "";
        super.load_table(path,'GET',titles,this.rowFunc);
    }

    static rowFunc(p){
        let tr_id = "tr" + p.id;
        let html = `
         <tr id='${tr_id}'>
            <td>${p.id}</td>
            <td onclick = 'model_setting.load_table_one(${p.id})'>${p.model_name}</td>
            <td>${p.auth}</td>
         </tr>`;
        return html
    }

    static load_table_one(id){
        let path = "/mobyheart/display-model-settings/" + id + "/";
        let tr_id = "tr" + id;
        let titles = ['Number','Detail Number','Item Content','Config Date','Config Basic','Config Max','Config Min','Score'];
        let button_url = '/mobyheart/save-modified-model-settings/';
        let req = this.ajax('GET',path);
        req.then((text)=>{
            let table_name = document.getElementById(tr_id).querySelectorAll("td:nth-child(2)")[0].innerHTML.trim(' ');
            let parsed = JSON.parse(text);
            this.rewrite_table_title('table_id',titles);
            let html = '';
            let counter = '';
            for(let p of parsed){
                html += this.display_model_details_content_html(p,counter);
                counter++;
            }
            document.getElementById("tbody").innerHTML = html;
            document.getElementById('tbody').setAttribute('name',table_name);
            this.display_two_buttons('button_id','model_setting.create_new_table',button_url);
        }).catch((status)=>{
            this.handle_err(status);
        });
    }

    static display_model_details_content_html(p,counter){
        let tr_id = "tr" + counter;
        let conf = ['config_date','config_basic','config_max','config_min','score'];
        let head = `<tr id='${tr_id}'>
        <td>${p.item_num}</td>
        <td>${p.item_detail_num}</td>
        <td>${p.item_content}</td>`;
        let end = "</tr>";
        let middle = this.make_ori_data_html(conf,counter,p,'model_setting.modify_input_chart');
        let html = head + middle + end;
        return html
    }

    static make_ori_data_html(conf,counter,p,func){
        let html = '';
        for(let c of conf){
            if (p[c].length === 0){
                html += `<td>${p[c]}</td>`
            } else {
                let id_name = c + counter;
                html += `<td ondblclick = ${func}('${id_name}') id='${id_name}'>${p[c]}</td>`;
            }
        }
        return html
    }

    static modify_input_chart(id_name){
        let input_id = "input_" + id_name;
        document.getElementById(id_name).innerHTML = `<input id='${input_id}'>`;
        document.getElementsByTagName('body')[0].setAttribute("onmousedown","model_setting.save_modified_input()");
    }

    static save_modified_input(){
        let inputs = document.getElementsByTagName('input');
        let td_id = '';
        if(inputs.length > 0){
            if(inputs[0].value.length > 0){
                for(let fragment of inputs){
                    let modified = fragment.value;
                    let splited = fragment.attributes[0].value.split("_");
                    if(splited.length === 2){
                        td_id = splited[1];
                    }else{
                        td_id = splited[1] + "_" + splited[2];
                    }
                    document.getElementById(td_id).innerHTML = modified;
                }
            }
        }
    }

    static create_new_table(path){
        let arr = [];
        let tbody = document.getElementById('tbody');
        let table_name = tbody.getAttribute('name');
        let rows = tbody.querySelectorAll('tr');
        for(let row of rows){
            let tds = row.querySelectorAll('td');
            arr.push(
                {
                    'item_num':tds[0].innerHTML,
                    'item_detail_num':tds[1].innerHTML,
                    'item_content':tds[2].innerHTML,
                    'config_date':tds[3].innerHTML,
                    'config_basic':tds[4].innerHTML,
                    'config_max':tds[5].innerHTML,
                    'config_min':tds[6].innerHTML,
                    'score':tds[7].innerHTML
                }
            )
        }
        let posted = {};
        posted[table_name] = arr;
        let jsoned = JSON.stringify(posted);
        this.ajax('POST',path,jsoned);
    }
}

class item_selection extends main{

    static load_table(){
        let titles = ['Number','Item','Plus','Minus'];
        this.ajax('GET','/home/');
        let req = this.ajax('GET','/mobyheart/load-items/');
        req.then((text)=>{
            this.rowFunc(text,titles);
        }).catch((status)=>{
            this.handle_err(status);
        });
    }

    static rowFunc(text,titles){
        this.rewrite_table_title('table_id',titles);
        this.display_two_buttons('button_id','item_selection.save_to_db');
        let parsed = JSON.parse(text);
        if(parsed.length === 0){
            throw 'parsed.length === 0';
        }
        let html = '';
        for(let p of parsed){
            let num = p[0];
            let item = p[1];
            html += this.make_one_row(num,item);
        }
        document.getElementById("tbody").innerHTML = html;
    }

    static make_one_row(num,item){
        let tr_id = "tr" + num;
        let html = `
        <tr id='${tr_id}'>
            <td>${num}</td>
            <td>${item}</td>
            <td><span class="glyphicon glyphicon-plus" onclick="item_selection.plus_minus('${tr_id}','plus')"></span></td>
            <td><span class="glyphicon glyphicon-minus" onclick="item_selection.plus_minus('${tr_id}','minus')"></span></td>
        </tr>`;
        return html
    }

    static verify_model_name_not_illegal(msg){
        if(msg === null){
            return true
        }
        let matched = msg.match(/[\w|_]+/);
        if (matched.length === 0){
            return true
        }
        let final = new Boolean();
        matched[0].length !== msg.length ?final = true:final = false;
        return final;
    }

    static save_to_db(){
        if (document.getElementsByClassName("success").length === 0){
            alert("please select one item at least");
            return
        }
        let path = "/mobyheart/is-unique-model-name/";
        let msg = prompt("please enter your model name");
        if (this.verify_model_name_not_illegal(msg)){
            alert("model name only supports that character/digit and flag '_' ");
            return
        }
        let j = JSON.stringify(msg);
        if (msg.length === 0){
            alert("model name is empty!");
            return
        }
        let req = this.ajax('POST',path,j);
        req.then((text)=>{
            this.model_name_legal_then_post(text,msg);
        }).catch((status)=>{
            this.handle_err(status);
        });
    }

    static model_name_legal_then_post(text,msg){
        let post_data = {};
        if (JSON.parse(text) === "false"){
            alert("this model name has existed");
            return
        }
        let nums = this.pick_all_success();
        post_data[msg] = nums;
        let req = this.ajax('POST',"/mobyheart/regist-model/",JSON.stringify(post_data));
        req.then((text)=>{
            alert(text);
        }).catch((status)=>{
            this.handle_err(status);
        })
    }

    static pick_all_success(){
        let nums = new Array();
        let success = document.getElementsByClassName("success");
        for(let i of success){
            try{
                nums.push(i.innerText[0]);
            }catch(err){
                this.handle_err(err);
                return
            }
        }
        return nums;
    }

    static plus_minus(id,flag){
        switch (flag){
            case 'plus':
                document.getElementById(id).setAttribute("class","success");
                break;
            case 'minus':
                document.getElementById(id).removeAttribute("class");
                break;
        }
    }
}




