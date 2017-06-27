package com.powermock.demo;

import org.apache.http.HttpResponse;
import org.apache.http.HttpStatus;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;


public class ChatbotSend {

    public static String WEBHOOK_TOKEN = "https://oapi.dingtalk.com/robot/send?access_token=03f0e99138b1d7c4a0e658803fdb4fac0e727e6709398534256e3daa3765fc6a";

    public static void main(String args[]) throws Exception{
        String textMsg = "{ \"msgtype\": \"text\", \"text\": {\"content\": \"我就是我, 是不一样的烟火\"},\"at\":{\"atMobiles\":[\"18566251523\",\"18520811268\"],\"isAtAll\":true}}";
        //String textMsgLink = "{ \"msgtype\": \"link\", \"link\": { \"text\": \"这个即将发布的新版本，创始人陈航（花名“无招”）称它为“红树林”。 而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是“红树林”？\",\"title\": \"时代的火车向前开\", \"picUrl\": \"https://gss1.bdstatic.com/9vo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=ca5abb5b7bf0f736ccf344536b3cd87c/29381f30e924b899c83ff41c6d061d950a7bf697.jpg\", \"messageUrl\": \"https://mp.weixin.qq.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI\" }}";
        String textMsgMD = "{\"msgtype\": \"markdown\",\"markdown\": { \"title\":\"杭州天气\",\"text\": \"#### **杭州天气**\n> 9度，西北风1级，空气良89，相对温度73%\\n\\n > ![screenshot](https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2476502197,211383670&fm=11&gp=0.jpg)\\n> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \"}}";
        ChatbotSend.sendMsg(textMsg);
        //ChatbotSend.sendText(textMsgLink);
        System.out.println(textMsgMD);
        //ChatbotSend.sendText(textMsgMD);
    }

    public static void sendMsg(String textMsg) throws Exception{
        HttpClient httpclient = HttpClients.createDefault();

        HttpPost httppost = new HttpPost(WEBHOOK_TOKEN);
        httppost.addHeader("Content-Type", "application/json; charset=utf-8");


        StringEntity se = new StringEntity(textMsg, "utf-8");
        httppost.setEntity(se);

        HttpResponse response = httpclient.execute(httppost);
        if (response.getStatusLine().getStatusCode()== HttpStatus.SC_OK){
            String result= EntityUtils.toString(response.getEntity(), "utf-8");
            System.out.println(result);
        }
    }
}