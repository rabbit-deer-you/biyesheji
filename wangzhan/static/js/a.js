var data1=[];
var data2=[];
var option={};	
var ID= document.getElementById("getid").getAttribute("data");
var tool = echarts.init(document.getElementById("tool"));
var month = echarts.init(document.getElementById("month"));
var tuijian = document.getElementById("tuijian");
var user = [];
user["1887683497"] = "平安哈尔滨";
user["2466412043"] = "新浪哈尔滨旅游";
user["1688383542"] = "哈尔滨身边事";
user["2477971432"] = "微博动漫";
user["1748075785"] = "哔哩哔哩弹幕网";
user["2410626252"] =   "AcFun弹幕视频网";
user["1263498570"] = "黄渤";
user["5187664653"] = "邓超";  
user["1751675285"] = "岳云鹏"; 
user["1854283601"] = "郭德纲"; 
user["2803301701"] = "人民日报"; 
user["2656274875"] = "央视新闻"; 
user["1826792401"] = "王思聪"; 
user["2714280233"] = "papi酱"; 
user["1563926367"] = "天才小熊猫"; 
user["2477339061"] = "艾克里里"; 
user["3217179555"] = "回忆专用小马甲"; 
user["1691761292"] = "叫兽易小星"; 
user["1742121542"] = "八卦我实在是太CJ了";   
user["1659041705"] = "穆雅斓"; 
user["1549362863"] = "张大奕eve"; 
user["1808624312"] = "章泽天"; 

	        // 指定图表的配置项和数据
$.ajax({
	dataType:"json",
	type:"get",
	url:"getTools",
	data:{
		"id":ID,
		"type":"tool"
	},
	success:function(data){
		$.each(data,function(key,value){
			data1.push(key);
			data2.push({value:value,name:key});
		});
		option = {
		    title : {
		        text: '用户使用平台统计',
		        x:'center'
		    },
		    tooltip : {
		        trigger: 'item',
		        formatter: "{a} <br/>{b} : {c} ({d}%)"
		    },
		    legend: {
		        orient: 'vertical',
		        left: 'left',
		        data: data1
		    },
		    series : [
		        {
		            name: '平台',
		            type: 'pie',
		            radius : '55%',
		            center: ['50%', '60%'],
		            data:data2,
		            itemStyle: {
		                emphasis: {
		                    shadowBlur: 10,
		                    shadowOffsetX: 0,
		                    shadowColor: 'rgba(0, 0, 0, 0.5)'
		                }
		            }
		        }
		    ]
		};
		tool.setOption(option);
		data1=[];
		data2=[];
		option={};
	}
});

	
var month_hash=["Jau","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Decm"];
$.ajax({
	dataType:"json",
	type:"get",
	url:"getMonth",
	data:{
		"id":ID,
		"type":"month"
	},
	success:function(data){
		for(var i=0;i<12;i++){
			data1.push(data[month_hash[i]]);
		}
		var option = {
		              title: {
		                text: '用户月份微博统计'
		              },
		              tooltip: {},
		              legend: {
		              		data:['数量']
		              },
		              xAxis: {
		              		data: ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月']
		              },
		              yAxis: {},
		              series: [{
		              		name: '数量',
		                	type: 'bar',
		                	data:data1
		               }]
		};
		month.setOption(option);
		data1=[];
		data2=[];
		option={};
	}
});

 /*!
   * Create an array of word objects, each representing a word in the cloud
   */
  var word_array = [];
  $.ajax({
	dataType:"json",
	type:"get",
	url:"getKeyword",
	data:{
		"id":ID,
		"type":"keyword",
		"num":60
	},
	success:function(data){
		for(var i =0;i<data.length;i++){
			word_array.push({text:data[i].key,weight:data[i].value,html:{data:data[i].key},handlers:{click: function() { str = $(this).attr("data"); wordMonth(str);}}});
		}
		$(function() {
    // When DOM is ready, select the container element and call the jQCloud method, passing the array of words as the first argument.
    			$("#cloud").jQCloud(word_array);
 		});
	}
});

function wordMonth(str){
	var div = document.getElementById("word_month");
	var tuijian = document.getElementById("tuijian");
	div.innerHTML= "";
	var wordMonth = echarts.init(div);
	var month_hash=["Jau","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Decm"];
	$.ajax({
		dataType:"json",
		type:"get",
		url:"getkeyword_month",
		data:{
			"id":ID,
			"type":"keyword",
			"keyword":"%27"+str+"%27"
		},
		success:function(data){
			for(var i=0;i<12;i++){
				data1.push(data[month_hash[i]]);
			}
			option = {
			    title: {
			        text: '用户关键词月份统计（'+str+'）'		    },
			    tooltip: {
			        trigger: 'axis'
			    },
			    grid: {
			        left: '3%',
			        right: '4%',
			        bottom: '3%',
			        containLabel: true
			    },
			    toolbox: {
			        feature: {
			            saveAsImage: {}
			        }
			    },
			    xAxis: {
			        type: 'category',
			        name:'月份',
			        boundaryGap: false,
			        data: ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月']
			    },
			    yAxis: {
			        type: 'value',
			        name:'数量'
			    },
			    series: [
			        {
			            name:'数量',
			            type:'line',
			            smooth:true,
			            stack: '总量',
			            data:data1
			        }
	   		    ]
			};

			wordMonth.setOption(option);
			data1=[];
			data2=[];
			option={};
		}
	});

	$.ajax({
		dataType:"json",
		type:"get",
		url:"getsimilar_user",
		data:{
			"id":ID,
			"keyword":"%27"+str+"%27"
		},
		success:function(data){
			tuijian.innerHTML = ""
			for(var i=0;i<data.length;i++){
				tuijian.innerHTML = tuijian.innerHTML+user[data[i]];
				if(i !== data.length-1){
					tuijian.innerHTML+=","
				}
			}
		}
	});
	document.getElementById("similar").style.display = "block";
}

document.getElementById("content_title").innerHTML += user[ID];