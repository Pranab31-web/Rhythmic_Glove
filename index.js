import express from "express";
// import { Server } from "socket.io";
// import { createServer } from "http";
import cors from "cors";
import cookieParser from "cookie-parser";
import path from 'path'
import mongoose  from "mongoose";
import signUpUser from './schema/signUpSchema.js'
import outputUser from "./schema/outPutSchema.js";
import { Server } from "socket.io";
import { createServer } from "http";
import dataSaved from "./schema/dataSaved.js";
import fs from 'fs'
const port = 3000
const app = express();
const server = createServer(app);
const io = new Server(server, {
  cors: {
    origin: ['http://localhost:3000'],
  }
})
app.use(
  cors({
    origin: "*",
    methods: ["GET", "POST"],
    credentials: true,
  })
);
app.use(cookieParser())
app.use(express.urlencoded({ extended: false }))
app.use(express.json())

app.set('view engine', 'ejs')
app.set('views', path.resolve('views'))
console.log(path.resolve('views'))
app.use(express.static(path.resolve('public')))



const connected_socket = io.on('connection', (socket) => {
  console.log("USER CONNECTED", socket.id)

  socket.emit("first", "THIS IS FIRST")
  
})
io.engine.on("connection_error", (err) => {
  console.log(err.req);      // the request object
  console.log(err.code);     // the error code, for example 1
  console.log(err.message);  // the error message, for example "Session ID unknown"
  console.log(err.context);  // some additional error context
});


mongoose.connect('mongodb://127.0.0.1:27017/hack').then((err)=>{
  console.log("connection is established")
}).catch((a)=>{
  throw a;
})

const middleware =(req,res,next)=>{
  const cookie = req.cookies
  if(Object.keys(cookie).length==0){
    return res.redirect('/login')
  }else{
    req.data = cookie
    next()
  }
}

app.get('/check',(req,res)=>{
  connected_socket.emit("check","hello this is ceck")
  res.end("hrllo")
})

app.get('/',middleware,(req,res)=>{
  console.log(req.cookies)
  if(req.cookies){
    console.log("cookies")
  }
  console.log(req.data)
    res.render('front_page',{'data':req.data})
})


app.post('/submit_instrument',  async (req,res)=>{
  console.log("qwerttdrgfgdfgdfgd")
  console.log(req.body)
  let data = req.body
  console.log(data)
  console.log(data.email)
  console.log(data.instrument)
  console.log(data.word_list)
  const dee = await outputUser.deleteMany({})
  
  const user = await outputUser.create({email:data.email,instrument:data.instrument,word:data.word_list,conversation:"no"})
    
  return res.json({"hello":"hello"})
})

app.get('/play_music',middleware,(req,res)=>{
  return res.render('play_music',{'data':req.data})
})

app.get('/signup',(req,res)=>{
    res.render('signup')
})
app.get('/current', async(req,res)=>{
  let data = await outputUser.find({})
  console.log(data)
  return res.json(data[0])
})

app.get('/conversation',middleware,(req,res)=>{

  return res.render('hands',{data:req.data})
})

app.get('/front_page',(req,res)=>{
  return res.render('front_page')
})

app.post('/signup',async(req,res)=>{
  console.log(req.body)
  const data  = req.body
  let userfind = await signUpUser.findOne({'email':data.email})
  
  if(userfind){
    return res.redirect('/login')
  }else{
    let creatUser = await signUpUser.create({email:data.email,username:data.username,password:data.password})
    let q = await dataSaved.create({email:data.email,data:""})
    return res.redirect('/login')
  }
})

app.post('/login',async(req,res)=>{
  let data = req.body
  let user = await signUpUser.findOne({'email':data.email})
  if(user){
    res.cookie('email',user.email)
    res.cookie('username',user.username)
    req.data = {'email':user.email,'username':user.username}
    return res.redirect('/')
  }else{
    return res.redirect('/signup')
  }
})

app.get('/login',(req,res)=>{
  res.render('login')
})

app.get('/selection',(req,res)=>{
  res.render('selection')
})

app.get('/third',middleware, async(req,res)=>{
  const dee = await outputUser.deleteMany({})
  
  const user = await outputUser.create({email:req.data.email,instrument:'',word:[],conversation:"yes"})
   
  res.render('third',{userEmail:req.data.email})
})

app.get('/secondMode/:id',(req,res)=>{
  console.log(req.params)
  connected_socket.emit("secondMode",req.params.id)
  res.send("hello")
})

app.get('/spaceMode/:id',(req,res)=>{
  console.log(req.params)
  connected_socket.emit("spaceMode",req.params.id)
  res.send("hello")
})


app.get('/suggestion/:id',(req,res)=>{
  const a = req.params.id
  const data = JSON.parse(fs.readFileSync('./example.json', 'utf-8'));
  let sendArr = new Array()
  let len = a.length
  data.forEach(element => {
      const word = element.word
      if(word.slice(0,len)==a){
        sendArr.push(element)
      }
  });
  connected_socket.emit("suggestion",req.params.id)

  res.send(sendArr)

})


app.get('/firstMode/suggestion/:id',(req,res)=>{
  const data = req.params.id
  connected_socket.emit("firstMode_suggestion",data)
  res.end("done 1")
})




app.get('/secondMode/suggestion/:id',(req,res)=>{
  const data = req.params.id
  connected_socket.emit("secondMode_suggestion",data)
  res.end("done 1")
})

app.get('/thirdMode/:id',(req,res)=>{
  let data = req.params.id
  connected_socket.emit("thirdMode",data)
  console.log("third mode data",data)
  res.send("hhello")
})

app.post('/submit',async(req,res)=>{
  let data = req.body
  console.log(data)
  let submit = await dataSaved.findOneAndUpdate({email:data.email},{data:data.data})
  res.send("hello")
})


server.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
