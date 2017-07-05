#!/usr/bin/python

my_account = Account("http://1679086725804112.mns.cn-beijing.aliyuncs.com", "LTAI2I65qtzofZLM", "v7V2M3vTxEdg94BHCq3azTMGJG90oM")
my_topic = my_account.get_topic("sms.topic-cn-beijing")
'''
Step 2. 设置SMS消息体（必须）
注：目前暂时不支持消息内容为空，需要指定消息内容，不为空即可。
'''
msg_body1 = "sms-message1."

'''
Step 3. 生成SMS消息属性，single=False表示每个接收者参数不一样，
'''
# 3.1 设置SMSSignName和SMSTempateCode
direct_sms_attr1 = DirectSMSInfo(free_sign_name="红火台餐饮云", template_code="SMS_71180601", single=False)
direct_sms_attr1.add_receiver(receiver="$YourReceiverPhoneNumber1")
direct_sms_attr1.set_params({"$YourSMSTemplateParamKey1": "$Value"})
'''
#Step 5. 生成SMS消息对象
'''
msg1 = TopicMessage(msg_body1, direct_sms = direct_sms_attr1)
try:
    '''
    Step 6. 发布SMS消息
    '''
    re_msg = my_topic.publish_message(msg1)
    print "Publish Message Succeed. MessageBody:%s MessageID:%s" % (msg_body1, re_msg.message_id)
except MNSExceptionBase,e:
    if e.type == "TopicNotExist":
        print "Topic not exist, please create it."
        sys.exit(1)