<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;

class GuestController extends Controller
{
    //
    public function stranger()
    {
        $strangers = DB::table('facestr_1')->simplePaginate(12);
        return view('guest_manager_str', ['strangers' => $strangers]);
    }

    public function ac()
    {
        $strangers = DB::table('face_1')->simplePaginate(12);
        return view('guest_manager_ac', ['strangers' => $strangers]);
    }

    public function change_ac(Request $request)
    {
        if (($request->name) != null) {
            $userid = Auth::id();
            if (($request->name) != null) {
                if(0==func::locapi('updateface', $request->face_token, $request->name, $userid, 0))
                    return back()->with('success', "修改成功");
            }
        }
        return back()->with('fail', "修改失败");
    }

    public function change_str(Request $request)
    {
        if (($request->name) != null) {
            $userid = Auth::id();
            if (($request->name) != null) {
                if(0==func::locapi('updateface', $request->face_token, $request->name, $userid, 1))
           return back()->with('success', "修改成功");
            }
        }
        return back()->with('fail', "修改失败");
    }
}
