import Axios from "axios";

let api = {
  async get_car_list() {
    const res = await Axios({
      url: "/cars",
      method: "get",
    });
    return res.data
      // return [
    //   { car_id: "沪A12345", color: "白色", series: "桑塔纳", type: "轿车" },
    //   { car_id: "沪A23456", color: "蓝色", series: "途安", type: "SUV" },
    // ];
  },
  get_client_list() {

    /* return [
      {
        client_id: '1',
        client_name: '王波',
        client_type: '个人',
        discount: '100',
        contact: '王波',
        tel: '136123123123',
        cars: [
          { car_id: "沪A12345", color: "白色", series: "桑塔纳", type: "轿车" },
          { car_id: "沪A23456", color: "蓝色", series: "途安", type: "SUV" },
        ]
      },
      {
        client_id: '2',
        client_name: '王义炜无敌有限公司',
        client_type: '公司',
        discount: '88',
        contact: '王义炜',
        tel: '180123241',
        cars: [
          { car_id: "沪B12345", color: "白色", series: "桑塔纳", type: "轿车" },
          { car_id: "沪C23456", color: "蓝色", series: "途安", type: "SUV" },
        ]
      }
    ] */
  },
  get_fix_list() {
    return [
      {
        "fix_id": "12345",
        "car_id": "沪A12345",
        "client_id": "123",
        "priority": "普通",
        "type": "中修",
        "pay": "现付",
        "in_time": "2022-01-10",
        "clerk_name": "王波",
        "clerk_id": "01",
        "est_time": "2022-01-16",
        "describe": "BOOM！"
      },
      {
        "fix_id": "56789",
        "car_id": "沪A56789",
        "client_id": "321",
        "priority": "加急",
        "type": "大修",
        "pay": "现付",
        "in_time": "2022-01-12",
        "clerk_name": "王波",
        "clerk_id": "01",
        "est_time": "2022-01-16",
        "describe": "BOOM！"
      },
    ]
  },
  get_job_list(fix_id) {
    return [
      {
        "job_id": "012",
        "job_name": "维修车头",
        "time": "5",
        "worker_id": "012",
        "worker_name": "机修",
        "status" : true,
      },
      {
        "job_id": "017",
        "job_name": "更换车灯",
        "time": "1",
        "worker_id": "012",
        "worker_name": "机修",
        "status" : false,
      }
    ]
  },
  get_report(){
    return {
      "client_name": "王义炜",
      "client_type": '个人',
      "discount": '80',
      "car_id": "沪A12345",
      "priority": "普通",
      "fix_type": "中修",
      "pay": "现付",
      "in_time": "2022-01-10",
      "clerk_name": "王波",
      "describe": "BOOM！",
      fix:[
        {
              "job_id":"012",
              "job_name":"维修车头",
              "time":"5",
              "worker_id":"012",
              "worker_name":"机修",
          "unit_price": 200,
          "subtotal": 1000 // 200*5 = 1000
      },
        {
              "job_id":"012",
              "job_name":"维修车屁股",
              "time":"2",
              "worker_id":"012",
              "worker_name":"机修",
          "unit_price": 100,
          "subtotal": 200
      }
      ],
    total : 1200
  }
  }

};
export default api;
