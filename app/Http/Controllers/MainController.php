<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MainController extends Controller
{
    //主界面默认显示
    public function index(){
        return view('main');
    }
//    侧边栏显示
    public function sidebar(){
        return view('sidebar');
    }
}
