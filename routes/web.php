<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::any('/', function () {
    return view('welcome');
});

Auth::routes();

Route::get('/home', 'HomeController@index')->name('home');
Route::get('/main', 'MainController@index')->name('main');
Route::get('/sidebar', 'MainController@sidebar')->name('sidebar');
Route::get('/capture', 'CaptureController@index')->name('capture');
Route::get('/today', 'TodayController@index')->name('today');
Route::get('/history', 'HistoryController@index')->name('history');
Route::get('/uploadimg', 'UploadimgController@index')->name('uploadimg');
Route::post('/upload_img', 'UploadimgController@upload')->name('upload_img');

Route::get('/cam_history', 'SettingController@cam_history')->name('cam_history');
Route::get('/upload_history', 'SettingController@upload_history')->name('upload_history');

Route::get('/today_ac', 'TodayController@ac')->name('today_ac');
Route::get('/today_str', 'TodayController@stranger')->name('today_str');
Route::get('/history_ac', 'HistoryController@ac')->name('history_ac');
Route::get('/history_str', 'HistoryController@stranger')->name('history_str');
Route::get('/home', 'HomeController@index')->name('home');
Route::get('/guest_manager_str', 'GuestController@stranger')->name('guest_manager_str');
Route::get('/guest_manager_ac', 'GuestController@ac')->name('guest_manager_ac');
Route::post('/history_change', 'HistoryController@change')->name('history_change');
Route::post('/today_change', 'TodayController@change')->name('today_change');
Route::post('/change_str', 'GuestController@change_str')->name('change_str');
Route::post('/change_ac', 'GuestController@change_ac')->name('change_ac');
Route::get('/delete_face', 'SettingController@delete_face')->name('delete_face');



