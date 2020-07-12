function appendMsg(selector, msg, username)
{
    msg =  $.parseJSON(msg);
    var msgBox = $('<div>');
    msgBox.addClass('message-box');
    if(msg['sender'] === username)
    {
        msgBox.addClass('self');
    }
    else
    {
        msgBox.addClass('others');
    }

    msgContent = $('<div>');
    msgContent.addClass('message-content');
    
    msgSender = $('<div>');
    msgSender.addClass('message-sender');
    msgSender.text(msg['sender'])

    msgText = $('<div>');
    msgText.addClass('message-text');
    msgText.text(" " + msg['content'])

    msgTime = $('<div>');
    msgTime.addClass('message-time');
    msgTime.text(msg['time'].substring(0, 22))

    msgContent.append(msgSender);
    msgContent.append(msgText);
    msgContent.append(msgTime);

    msgAvatar = $('<i>');
    msgAvatar.addClass('message-avatar');
    msgAvatar.addClass('fas');
    msgAvatar.addClass('fa-user-circle');
    msgAvatar.addClass('fa-4x');
    msgAvatar.css('color', msg['style']);

    msgBox.append(msgAvatar);
    msgBox.append(msgContent);

    msgBox.addClass('row');

    $(selector).append(msgBox);
    $(selector).animate({scrollTop:$(selector)[0].scrollHeight},'500');
}
