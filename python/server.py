# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging
import json
import grpc
import time
import os
import redis
import json_pb2
import json_pb2_grpc


class JSon(json_pb2_grpc.jsonServiceServicer):

	
	def JsonFunc(self, request, context):
		user_id = 0
		user = {

		"name":request.Name,
		"surname":request.Surname,
		"ipaddress":request.IpAddress,
		"email":request.Email,
		"gender":request.Gender,
		"country":request.Country,
		"username":request.Username,
		"agent":request.Agent
		}
		if(user_id % 1000 == 0 and user_id >999):
			user_id +=1 

		user_json_dump = json.dumps(user)
		setID = user_id*1000+int(request.ID)
		client.set(setID,user_json_dump)
		
		time.sleep(0.08)
		#print("Name:{}\n \
			#Surname:{}\n\
			#Agent:{}\n\
			#Ipaddress:{}\n\
			#Gener:{}\n".format(request.Name,request.Surname,request.Agent,request.IpAddress,request.Gender))
		user_redis = client.get(setID)
		print("Name:{} ".format(json.loads(user_redis.decode("utf-8"))["name"]))
		
		return json_pb2.jsonResponse(message="ID:{} ".format(request.ID))


def serve():
	server = grpc.server(futures.ThreadPoolExecutor())
	json_pb2_grpc.add_jsonServiceServicer_to_server(JSon(), server)
	server.add_insecure_port('0.0.0.0:50051')
	
	server.start()
	server.wait_for_termination()


if __name__ == '__main__':
	logging.basicConfig()
	client = redis.Redis(host='redis', port=6379)
	serve()
