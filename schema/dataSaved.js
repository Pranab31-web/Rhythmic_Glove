import mongoose from "mongoose";

const signUpSchema = new mongoose.Schema({
    email:{
        type:String,
        require:true
    },
    data:{
        type:String
        
    }
})

const dataSaved = new mongoose.model("save", signUpSchema);

export default  dataSaved ;