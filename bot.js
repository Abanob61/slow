const Discord = require('discord.js');

const client = new Discord.Client();

 

client.on('ready', () => {

    console.log('I am ready!');
    client.user.setActivity('SlowBall', { type: 'PLAYING' });
});

 

client.on('message', message => {

    if (message.content === '!ping') {

       message.reply('pong');

       }

});
client.login("NTIzMTcwMzQ4Nzg3Njk1NjE4.DwB4ig.iv09OalIU4hX8ad5N1dQCUGduZw");
