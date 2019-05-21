<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class func extends Controller
{
    //本地socket连接
    static public function locapi($key,$key1="",$key2="",$key3="",$key4=""){
        $socket = socket_create(AF_INET,SOCK_STREAM,SOL_TCP);
        socket_set_option($socket, SOL_SOCKET, SO_RCVTIMEO, array("sec" => 6, "usec" => 0));
        socket_set_option($socket, SOL_SOCKET, SO_SNDTIMEO, array("sec" => 6, "usec" => 0));
        if(socket_connect($socket,env('LOCAPI_ADDR'),env('LOCAPI_PORT')) == false){
            echo 'connect fail massege:'.socket_strerror(socket_last_error());
        }else{

            $message = array('key'=>$key,'key1'=> $key1, 'key2'=>$key2, 'key3'=> $key3, 'key4'=>$key4);
            $message=json_encode($message);

            if(socket_write($socket,$message,strlen($message)) == false){
                echo 'fail to write'.socket_strerror(socket_last_error());

            }else{
                echo 'client write success'.PHP_EOL;
                //读取服务端返回来的套接流信息
                $callback = socket_read($socket,102400);
                    echo 'server return message is:'.PHP_EOL.$callback;

            }
        }
        socket_close($socket);//工作完毕，关闭套接流
    }
    static public function update_face_str($id,$name){

    }

}
