<?php
/**
 * 用户数据/ 用户设备维护PHP 脚本
 * Created by PhpStorm
 * User: wsl
 * Date: 2017/12/21
 * Time: 10:38
 */
include "./lib/EasyDB/EasyDB.php";

$config = array(
    'host'     => '127.0.0.1',//数据库连接ip,默认本机
    'port'     => 3306,       //端口号,默认3306
    'username' => 'root',     //用户名,默认root
    'password' => '123456',   //密码,默认空
    'dbname'   => 'tutorial', //数据库名字
    'charset'  => 'utf8'      //字符集,默认utf8
);

$db = new EasyDB($config);


