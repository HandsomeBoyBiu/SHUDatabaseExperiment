<template>
  <div class="app-container">
    <div class="center">
      <h1>报价单</h1>
      <el-descriptions border>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-user"></i>
            客户姓名
          </template>
          {{ this.table_data.client_name }}
        </el-descriptions-item>

        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-s-ticket"></i>
            折扣率
          </template>
          {{ this.table_data.discount }}
        </el-descriptions-item>

        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-s-finance"></i>
            结算方式
          </template>
          {{ this.table_data.pay }}
        </el-descriptions-item>

        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-truck"></i>
            车牌号
          </template>
          {{ this.table_data.car_id }}
        </el-descriptions-item>

        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-timer"></i>
            维修类型
          </template>
          {{ this.table_data.priority }}
        </el-descriptions-item>

        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-tickets"></i>
            作业分类
          </template>
          {{ this.table_data.fix_type }}
        </el-descriptions-item>

        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-time"></i>
            进厂时间
          </template>
          {{ this.table_data.in_time }}
        </el-descriptions-item>

        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-service"></i>
            业务员
          </template>
          {{ this.table_data.clerk_name }}
        </el-descriptions-item>
      </el-descriptions>

      <el-descriptions direction="vertical" border>
        <el-descriptions-item :span="3">
          <template slot="label">
            <i class="el-icon-s-release"></i>
            故障描述
          </template>
          {{ this.table_data.describe }}
        </el-descriptions-item>

        <el-descriptions-item :span="3">
          <template slot="label">
            <i class="el-icon-s-release"></i>
            维修项目
          </template>
          <el-table :data="this.table_data.fix">
            <el-table-column label="项目编号" prop="job_id" />
            <el-table-column label="项目名称" prop="job_name" />
            <el-table-column label="维修员编号" prop="worker_id" />
            <el-table-column label="维修员工种" prop="worker_name" />
            <el-table-column label="工时" prop="time" />
            <el-table-column label="单价" prop="unit_price" />
            <el-table-column label="小计" prop="subtotal" />
          </el-table>
        </el-descriptions-item>

        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-coin"></i>
            总计
          </template>
          <div class="total">
            <div>总计：{{ this.table_data.total }} ¥</div>
            <div>优惠：{{ Math.round(this.table_data.total * (1 - this.table_data.discount / 100)) }} ¥</div>
            <div>应付：{{ Math.round((this.table_data.total * this.table_data.discount) / 100) }} ¥</div>
          </div>
        </el-descriptions-item>
      </el-descriptions>
    </div>
  </div>
</template>

<script>
import api from "@/utils/api";
import Axios from "axios";
export default {
  data() {
    return {
      table_data: [],
    };
  },
  mounted() {
    this.fix_id = this.$route.query.fix_id;
    // this.table_data = api.get_report();
    Axios({
      url: "/getreport?fix_id=" + this.fix_id,
      method: "get",
    }).then((res) => {
      console.log(res.data);
      this.table_data = res.data;
    });
    this.table_data.total = 0;
    for (let i of this.table_data.fix) {
      console.log(i.subtotal);
      this.table_data.total += i.subtotal;
    }
    console.log(this.table_data.total);
  },
  methods: {
    to_job(fix_id) {
      this.$router.push({ path: "/reg/job_reg", query: { fix_id } });
    },
  },
};
</script>

<style>
.total {
  padding: 0 0 0 5px;
  font-size: medium;
  font-weight: bold;
}
.center {
  width: 800px;
  margin: 0 auto;
  text-align: center;
}
el-descriptions {
  display: inline-block;
}
</style>