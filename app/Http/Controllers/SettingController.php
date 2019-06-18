<?php

namespace App\Http\Controllers;

use App\Http\Controllers\func;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;

class SettingController extends Controller
{
    //
    public function index(){

        return view("setting");
    }
    public function cam_history()
    {
        $strangers = DB::table('cam_photo')->simplePaginate(12);
        return view("cam_history", ['strangers' => $strangers]);
    }
    public function upload_history()
    {
        $strangers = DB::table('photo')->simplePaginate(12);
        return view("upload_history", ['strangers' => $strangers]);
    }

    public function change(Request $request)
    {
        //dump($request);
        $userid=Auth::id();
        if(($request->name)!=null){
            func::locapi('updateface',$request->face_token,$request->name,$userid,0);
        }
        return back();
    }
    public function delete(){
        func::locapi('delete');
        return back();
    }
    public function delete_face(){
        if(func::locapi('remove'))
            return back()->with('success',"清除成功");
        return back()->with('fail',"清除失败");

    }
}
