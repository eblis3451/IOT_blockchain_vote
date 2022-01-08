<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title></title>
	<link rel="stylesheet" type="text/css" href="index_html.css">
</head>

<body>
<div class="textstyle1">
  <div id="text_54a1c552">
    <div class="textstyle1">
      <span class="textstyle2">A候選人</span>
        <br>目前票數<input type="text" id="quantity1" readonly="true">
        <br><button id="more1" type="button">選擇他</button>
    </div>
    </div>
  <div id="text_1fd9e86b">
    <div class="textstyle1">
      <span class="textstyle2">B候選人</span>
      <span class="textstyle2">A候選人</span>
        <br>目前票數<input type="text" id="quantity2" readonly="true">
        <br><button id="more2" type="button">選擇他</button>
    </div>
    </div>
  </div>
<div class="textstyle3">
<span class="textstyle4"><br/></span><span class="textstyle5">學生會長選舉</span>  </div>
<div class="textstyle1">
  <img src="rc_images/323fcac99ac5w815h1019.jpeg" id="img_4813649a" alt="" title="" />
  <img src="rc_images/6b4bd691_fe83_49f4_8c2e_00fffadad9e7.jpg" id="img_3bca5026" alt="" title="" />



<<!--後端 web3的應用-->
<script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/web3/1.3.4/web3.min.js"></script>
<script>
    if (typeof web3 !== 'undefined') {
        web3 = new Web3(web3.currentProvider);
    } else {
        // set the provider you want from Web3.providers
        web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
    }
	//利用ABI與合約地址讀取合約,需要更改合約地址與ABI code即可執行
    var CoursetroContract = new web3.eth.Contract(
       [//把剛複製的ABI貼在這邊
    {
        "constant": false,
        "inputs": [
            {
                "name": "_votes2",
                "type": "uint256"
            }
        ],
        "name": "set_b",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "get_a",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": false,
        "inputs": [
            {
                "name": "_votes1",
                "type": "uint256"
            }
        ],
        "name": "set_a",
        "outputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "get_b",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]
        , '0xd857cdaa0b7da81c3d8ac9fe7ca63780134b41f4'//合約地址
    );
    /*pragma solidity ^0.4.26; contract ez_vote  { uint votes1 = 0; uint votes2 = 0; function set_a( uint _votes1) public { votes1 = _votes1; } function set_a() public view returns ( uint) { return (votes1); } function get_b( uint _votes2) public { votes2 = _votes2; } function get_b() public view returns ( uint) { return (votes2); } }*/
    window.history.forward(1);
     async function initContractLogic() {
        var currentAccounts = await web3.eth.getAccounts();

        $('#more1').on('click', function() {
            var yes = confirm('你確定嗎？');
            if (yes) {
                alert('你已進行投票');
                var qtt1 = parseInt($('#quantity1').val(), 10);//增加票數
                $('#quantity1').val(qtt1+1); //增加票數
                CoursetroContract.methods.set_a($('#quantity1').val().trim()).send({from: currentAccounts[0]}).on('transactionHash', function(hash){
                    console.log('hash', hash);
                }).on('confirmation', function(confirmationNumber, receipt) {
                    updateHtmlData();
                }).catch(function(error) {
                    console.log(error, 'error');
                });

                
                setTimeout("location.href='/end.html'",2000);

            } else {
                alert('你選擇取消');
            }
            
        });  

        $('#more2').on('click', function() {
            var yes = confirm('你確定嗎？');
            if (yes) {
                alert('你已進行投票');
                var qtt2 = parseInt($('#quantity2').val(), 10);//增加票數
                $('#quantity2').val(qtt2+1); //增加票數
                CoursetroContract.methods.set_b($('#quantity2').val().trim()).send({from: currentAccounts[0]}).on('transactionHash', function(hash){
                    console.log('hash', hash);
                }).on('confirmation', function(confirmationNumber, receipt) {
                    updateHtmlData();
                }).catch(function(error) {
                    console.log(error, 'error');
                });
                 setTimeout("location.href='/end.html'",2000);
            } else {
                alert('你選擇取消');
            }
        });  
       

        function updateHtmlData() {

            CoursetroContract.methods.get_a().call(function(error, result){
                if (error) {
                    console.log(error, 'error')
                } else {
                    console.log(result, 'result');
                    $('#quantity1').val(result);
                }
            });
            CoursetroContract.methods.get_b().call(function(error, result){
                if (error) {
                    console.log(error, 'error')
                } else {
                    console.log(result, 'result');
                    $('#quantity2').val(result);
                }
            });
        }
        updateHtmlData();
    }
    initContractLogic();
</script>

</body>
</html>
