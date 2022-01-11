let api = {
  get_car_list() {
    return [
      { car_id: "沪A12345", color: "白色", series: "桑塔纳", type: "轿车" },
      { car_id: "沪A23456", color: "蓝色", series: "途安", type: "SUV" },
    ];
  },
  get_client_list() {
    return [
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
        client_name: '王义炜',
        client_type: '个人',
        discount: '88',
        contact: '王义炜',
        tel: '180123241',
        cars: [
          { car_id: "沪B12345", color: "白色", series: "桑塔纳", type: "轿车" },
          { car_id: "沪C23456", color: "蓝色", series: "途安", type: "SUV" },
        ]
      }
    ]
  }

};
export default api;
