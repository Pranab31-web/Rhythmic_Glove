import mongoose from "mongoose";

const signUpSchema = new mongoose.Schema({
    username:{
        type:String,
        required:true
    },
    email:{
        type:String,
        required:true,
        unique:true
    },
    password:{
        type:String,
        required:true
        
    }
})

const signUpUser = new mongoose.model("user", signUpSchema);

export default  signUpUser ;