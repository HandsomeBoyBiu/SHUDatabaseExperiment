<template>
  <div class="app-container">
    <el-tabs v-model="active_tab">
      <el-tab-pane label="客户登记" name="client">
        <el-form ref="client_form" :model="client_form" label-width="100px" style="max-width: 1200px">
          <el-row type="flex" justify="left">
            <el-col :span="8">
              <el-form-item label="客户名称">
                <el-input v-model="client_form.client_name" @input="on_client_name_change" />
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="客户类型">
                <el-radio-group v-model="client_form.client_type" @change="on_client_type_change">
                  <el-radio label="单位" />
                  <el-radio label="个人" />
                </el-radio-group>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="折扣率(%)">
                <el-input-number
                  v-model="client_form.discount"
                  :min="1"
                  :max="100"
                  size="small"
                  controls-position="right"
                />
              </el-form-item>
            </el-col>
          </el-row>

          <el-row type="flex" justify="left">
            <el-col :span="12">
              <el-form-item label="联系人">
                <el-input v-model="client_form.contact" :disabled="contact_disable" />
              </el-form-item>
            </el-col>
            <el-col :span="12">
              <el-form-item label="手机号">
                <el-input v-model="client_form.tel" />
              </el-form-item>
            </el-col>
          </el-row>
          <el-form-item label="车牌号">
            <el-select v-model="client_form.car_id" filterable>
              <el-option v-for="item in car_list" :key="item.id" :value="item.id" :label="item.id" />
            </el-select>
            <el-button @click="bind_add_car" type="primary" icon="el-icon-plus" size="small" plain> 新增 </el-button>
            颜色:{{ selected_car.color }} 车型:{{ selected_car.series }} 车辆类别:{{ selected_car.type }}
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="bind_submit_client"> 提交 </el-button>
          </el-form-item>
        </el-form>
        <!--  -->
      </el-tab-pane>
      <el-tab-pane label="车辆登记" name="car">
        <el-form ref="car_form" :model="car_form" label-width="100px" style="width: 80%">
          <el-form-item label="车牌号">
            <el-input v-model="car_form.car_id" />
          </el-form-item>
          <el-form-item label="颜色">
            <el-input v-model="car_form.car_color" />
          </el-form-item>
          <el-form-item label="车型">
            <el-input v-model="car_form.car_series" />
          </el-form-item>
          <el-form-item label="车辆类别">
            <el-select v-model="car_form.car_type">
              <el-option v-for="item in types" :key="item" :label="item" :value="item" />
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="bind_submit_car"> 提交 </el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import api from '@/utils/api';
import Axios from 'axios';
export default {
  data() {
    return {
      client_form: {
        client_id: "",
        client_name: "",
        client_type: "",
        discount: "100",
        contact: "",
        tel: "",
        car_id: "",
      },
      car_form: {
        car_id: "",
        car_color: "",
        car_series: "", // 车型
        car_type: "", // 车辆类别
      },
      car_list: [],
      types: ["轿车", "SUV", "面包车", "卡车"],
      contact_disable: false,
      active_tab: "client",
    };
  },
  mounted() {
    this.car_list = api.get_car_list();
  },
  computed: {
    selected_car: function () {
      let ret = { color: "", series: "", type: "" };
      console.log(this.car_list)
      // if (this.car_list != []){
      //   ret = this.car_list.filter((car) => car.id.indexOf(this.client_form.car_id))[0];
      // }
      return ret;
    },
  },
  methods: {
    // get_car_list() {
    //   this.car_list = [
    //     { id: "沪A12345", color: "白色", series: "桑塔纳", type: "轿车" },
    //     { id: "沪A23456", color: "蓝色", series: "途安", type: "SUV" },
    //   ];
    // },
    on_client_type_change() {
      if (this.client_form.client_type == "个人") {
        this.contact_disable = true;
        this.client_form.contact = this.client_form.client_name;
      } else {
        this.contact_disable = false;
      }
    },
    on_client_name_change() {
      // console.log(this.client_form.client_name)
      if (this.client_form.client_type == "个人") {
        this.client_form.contact = this.client_form.client_name;
      }
    },
    // car_id_suggestion(query, callback) {
    //   console.log(query);
    //   let car_list = this.car_list;
    //   let t = car_list.filter((car) => car.id.toLowerCase().indexOf(query.toLowerCase()) != -1);
    //   let ret = t.map((i) => {
    //     return { value: i.id };
    //   });
    //   console.log(ret);
    //   callback(ret);
    // },
    bind_add_car() {
      this.active_tab = "car";
    },
    bind_submit_car() {
      // Axios.post('/car/', this.car_form);
      Axios(
        {
          url:'/car/',
          method: 'post',
          crossdomain: true,
          data :this.car_form
        }
      ).then(res=>{console.log(res.data)});
      console.log(JSON.stringify(this.car_form));
      this.car_list = api.get_car_list();
      this.client_form.car_id = this.car_form.car_id;
      this.$message({
        message: "车辆登记成功",
        type: "success",
      });
      this.active_tab = "client";
    },
    bind_submit_client() {
      Axios.post('/client', this.client_form);
      // Axios.post('localhost:9999', this.client_form)
      console.log(JSON.stringify(this.client_form));
      this.$message({
        message: "客户登记成功",
        type: "success",
      });
    },
    // selected_car() {

    // }
  },
};
</script>