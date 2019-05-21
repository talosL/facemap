<?php

namespace App\Http\Controllers;

use function foo\func;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Auth;
class HistoryController extends Controller
{
    //
    public function index()
    {
        return view("history");
    }

    public function ac()
    {
        $strangers = DB::table('day')->simplePaginate(12);
        return view("history_ac", ['strangers' => $strangers]);
    }

    public function stranger()
    {
        $strangers = DB::table('day_str')->simplePaginate(12);
        return view("history_str", ['strangers' => $strangers]);
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
}
