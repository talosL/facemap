<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class CaptureController extends Controller
{
    //
    public function index(Request $request){
        if($request->act==1){
            if(1==func::locapi('takephoto'))
            {
                $res=DB::table('cam_photo')->orderBy('time','desc')->get();
                //dump($res[0]->face_name1);
                return view("capture")->with(['ret'=>$res[0]]);
            }
            else
                return view("capture")->with(['res'=>"拍照失败，请检查监控是否开启"]);
        }

        return view("capture");
    }
}
