<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="100px" style="max-width: 1200px">
      <el-form-item label="车牌号">
        <el-select v-model="form.car_id" filterable>
          <el-option v-for="item in car_list" :key="item.id" :value="item.id" :label="item.id" />
        </el-select>
      </el-form-item>
      <el-form-item label="维修类型">
        <el-radio-group v-model="form.priority">
          <el-radio-button label="加急" />
          <el-radio-button label="普通" />
        </el-radio-group>
      </el-form-item>
      <el-form-item label="作业分类">
        <el-radio-group v-model="form.type">
          <el-radio-button label="小修" />
          <el-radio-button label="中修" />
          <el-radio-button label="大修" />
        </el-radio-group>
      </el-form-item>
      <el-form-item label="结算方式">
        <el-radio-group v-model="form.pay">
          <el-radio-button label="现付" />
          <el-radio-button label="月结" />
        </el-radio-group>
      </el-form-item>
      <el-form-item label="进厂时间">
        <el-date-picker v-model="form.in_time" type="date" />
      </el-form-item>
      <el-form-item label="业务员">
        <el-input v-model="form.clerk_name" class="short" />
      </el-form-item>
      <el-form-item label="业务员编号">
        <el-input v-model="form.clerk_id" class="short" />
      </el-form-item>
      <el-form-item label="预计完工时间">
        <el-date-picker v-model="form.est_time" />
      </el-form-item>
      <el-form-item label="故障描述">
        <el-input v-model="form.describe" type="textarea" :rows="5" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="bind_submit"> 提交 </el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      form: {
        car_id: "",
        priority: "普通",
        type: "",
        pay: "",
        in_time: "",
        clerk_name: "",
        clerk_id: "",
        est_time: "",
        describe: "",
      },
      car_list: [],
    };
  },
  mounted() {
    Axios({
      url: "/cars",
      method: "get",
    }).then((res) => {
      this.car_list = res.data;
    });
    console.log(this.car_list);
  },
  methods: {
    bind_submit() {
      Axios({
        url: "/fix",
        method: "post",
        data: this.form,
      }).then((res) => {
        console.log(res);
        this.$message({
          message: "维修委托登记成功",
          type: "success",
        });
        this.form = {
          car_id: "",
          priority: "普通",
          type: "",
          pay: "",
          in_time: "",
          clerk_name: "",
          clerk_id: "",
          est_time: "",
          describe: "",
        };
      });
    },
  },
};
</script>
