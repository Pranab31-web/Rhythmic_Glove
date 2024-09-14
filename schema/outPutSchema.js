import mongoose from "mongoose";

const signUpSchema = new mongoose.Schema({
    email:{
        type:String,
        required:true
    },
    instrument:{
        type:String,
        
        
    },
    word:{
        type:Object,
        
        
    },
    conversation:{
        type:String,
        default:'no'
    }
})

const outputUser    = new mongoose.model("output", signUpSchema);

export default  outputUser ;