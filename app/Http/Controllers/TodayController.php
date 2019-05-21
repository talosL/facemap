<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use App\Http\Controllers\func;
class TodayController extends Controller
{
    //
    public function index(){
        //$strangers=DB::table('today')->simplePaginate(16);
        return view("today");
}
public function ac(){
    $strangers=DB::table('today')->simplePaginate(16);
    return view("today_ac",['strangers'=>$strangers]);
}
public function stranger(){
    $strangers=DB::table('today_str')->simplePaginate(16);
    return view("today_str",['strangers'=>$strangers]);
}
}
