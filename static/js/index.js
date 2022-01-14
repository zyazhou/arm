
var app=new Vue({
	el:".app",
	data:{
		fre:0,
		info:0,
		led:0,
	},
	methods:{

		ledon:function(){
			this.led=1;
			var that=this;
			var lbt = "";
			console.log("response.data")
			var params = new URLSearchParams();
			params.append('led',1);
			axios.post("http://10.102.103.121:5000/ledon", params)
			/*axios.get("http://127.0.0.1:5000/user_login?username=this.username&passwd=this.passwd")*/
			/*axios.get("http://127.0.0.1:5000/user_login/"+this.username+'/'+this.passwd)*/
			.then(function(response){
				lbt += '<li><p>LED状态:打开</li>';
					
				$("#ul_listled").empty()
				$("#ul_listled").append(lbt);
				console.log(response.data)	
			},function(err){
				alert('error')
				console.log('no')
				})
		},
		ledoff:function(){
			this.led=0;
			var that=this;
			var lbt = "";
			console.log("response.data")
			var params = new URLSearchParams();
			params.append('led',0);
			axios.post("http://10.102.103.121:5000/ledoff", params)
			/*axios.get("http://127.0.0.1:5000/user_login?username=this.username&passwd=this.passwd")*/
			/*axios.get("http://127.0.0.1:5000/user_login/"+this.username+'/'+this.passwd)*/
			.then(function(response){
					lbt += '<li><p>LED状态:关闭</li>';
						
					$("#ul_listled").empty()
					$("#ul_listled").append(lbt);
				console.log(response.data)	
			},function(err){
				alert('error')
				console.log('no')
				})
		},
		
		pwmon:function(){
			
			var that=this;
			var lbt = "";
			var params = new URLSearchParams();
			params.append('fre',that.fre);
		
			axios.post("http://10.102.103.121:5000/pwmon", params)
			/*axios.get("http://127.0.0.1:5000/user_login?username=this.username&passwd=this.passwd")*/
			/*axios.get("http://127.0.0.1:5000/user_login/"+this.username+'/'+this.passwd)*/
			.then(function(response){
					lbt += '<li><p>PWM已开启 </li>';
						
					$("#ul_listpwm").empty()
					$("#ul_listpwm").append(lbt);
				console.log(response.data)	
			},function(err){
				alert('error')
				console.log('no')
				})
		},
		
		pwmoff:function(){
			this.fre=0;
			var that=this;
			var lbt = "";
			var params = new URLSearchParams();
			axios.post("http://10.102.103.121:5000/pwmoff",params)
			/*axios.get("http://127.0.0.1:5000/user_login?username=this.username&passwd=this.passwd")*/
			/*axios.get("http://127.0.0.1:5000/user_login/"+this.username+'/'+this.passwd)*/
			.then(function(response){
				lbt += '<li><p>PWM已关闭 </li>';
					
				$("#ul_listpwm").empty()
				$("#ul_listpwm").append(lbt);
				console.log(response.data)	
			},function(err){
				alert('error')
				console.log('no')
				})
		},
		
			
		update:function(){
			var lbt1 = "";
			var lbt2 = "";
			var led_s=0;
			var freq=0;
			var that=this;
			axios.post("http://10.101.163.58:5000/update")
			.then(function(response){
				led_s=response.data['led'];
				freq=response.data['fre'];
				console.log(led_s)
				console.log(freq)
				if(freq>0&&freq<=10000)
				{
					that.fre=freq;
					lbt2 += '<li><p>PWM已开启 </li>';
				}
				else{
					that.fre=freq;
					lbt2 += '<li><p>PWM已关闭 </li>';
				}
			
				if(led_s==1)
				{
					
					that.led=led_s;
					lbt1 += '<li><p>LED已开启 </li>';
				}
				else{
				
					that.led=led_s;
					lbt1 += '<li><p>LED已关闭 </li>';
				}
					
				$("#ul_listpwm").empty()
				$("#ul_listled").empty()
				$("#ul_listled").append(lbt1);
				$("#ul_listpwm").append(lbt2);
				console.log(response.data)	
			},function(err){
				alert('error')
				console.log('no')
				})
			
		}

	},
	
})
