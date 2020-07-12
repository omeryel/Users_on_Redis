package main

import (
	"context"
	"fmt"
	"./hellopb"
	"google.golang.org/grpc"
	"log"
	"encoding/json"
    "io/ioutil"
    "os"
    "strconv"
    "time"
)


type User struct {
	Id       int      `json:"id"`
    Name     string   `json:"first_name"`
    Surname   string  `json:"last_name"`
    Email    string   `json:"Email"`
    Gender   string   `json:"gender"`   
    IPaddress string   `json:"ip_address"`
    Username   string   `json:"user_name"`
    Agent       string   `json:"agent`
    Country     string   `json:"country"`
}


func main() {
	fmt.Println("Hello client running ...")

	opts := grpc.WithInsecure()
	cc, err := grpc.Dial("localhost:50051", opts)
	if err != nil {
		log.Fatal(err)
	}
	defer cc.Close()

    files, err := ioutil.ReadDir("./jsons")
    if err != nil {
        log.Fatal(err)
    }

    for _, f := range files {

    	jsonFile, err := os.Open("./jsons/"+f.Name())
        // if we os.Open returns an error then handle it
        if err != nil {
            fmt.Println(err)
        }

        fmt.Println("Successfully Opened "+ f.Name())
        // defer the closing of our jsonFile so that we can parse it later on
        defer jsonFile.Close()

        // read our opened xmlFile as a byte array.
        byteValue, _ := ioutil.ReadAll(jsonFile)
     
        // we initialize our Users array
        var user []User

        // we unmarshal our byteArray which contains our
        // jsonFile's content into 'users' which we defined above
        json.Unmarshal([]byte(byteValue), &user)

         for i := 0; i < len(user); i++ {
        	
            
            time.Sleep(70 * time.Millisecond)

            client := hellopb.NewJsonServiceClient(cc)
    		request := &hellopb.JsonRequest{ID: strconv.Itoa(user[i].Id), Name: user[i].Name,Surname: user[i].Surname,Email: user[i].Email,Gender: user[i].Gender,IpAddress: user[i].IPaddress,Agent: user[i].Agent,Country:user[i].Country,Username:user[i].Username}

    		client.JsonFunc(context.Background(), request)
    		//fmt.Printf("Receive response => [%v]", resp.Message)
        }
        
    }
    fmt.Printf("Press Ctrl+C to Exit \n")
	
}
