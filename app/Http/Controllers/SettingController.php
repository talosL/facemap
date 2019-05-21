<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Http\Controllers\func;
class SettingController extends Controller
{
    //
    public function index(){

        return view("setting");
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
