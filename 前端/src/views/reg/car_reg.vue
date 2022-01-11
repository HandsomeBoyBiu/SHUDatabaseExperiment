<template>
  <div class="app-container">
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
  </div>
</template>

<script>
import api from "@/utils/api";
import Axios from "axios";
export default {
  data() {
    return {
      car_form: {
        car_id: "",
        car_color: "",
        car_series: "", // 车型
        car_type: "", // 车辆类别
      },
      types: ["轿车", "SUV", "面包车", "卡车"],
    };
  },
  mounted() {
    this.car_list = api.get_car_list();
  },
  computed: {
  },
  methods: {
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

    bind_add_car() {
      this.active_tab = "car";
    },
    bind_submit_car() {
      // Axios.post('/car/', this.car_form);
      Axios({
        url: "/car/",
        method: "post",
        crossdomain: true,
        data: this.car_form,
      }).then((res) => {
        console.log(res.data);
      });
      console.log(JSON.stringify(this.car_form));
      this.$message({
        message: "车辆登记成功",
        type: "success",
      });
      this.active_tab = "client";
    },
    bind_submit_client() {
      Axios.post("/client", this.client_form);
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