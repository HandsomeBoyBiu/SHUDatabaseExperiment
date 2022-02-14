<template>
  <div class="app-container">
    <h3>派工单</h3>
    <p>单号：{{ this.fix_id }}</p>
    <el-table :data="table_data">
      <el-table-column label="维修项目编号" prop="job_id" />
      <el-table-column label="维修项目" prop="job_name" />
      <el-table-column label="工时" prop="time" />
      <el-table-column label="维修员编号" prop="worker_id" />
      <el-table-column label="维修员工种" prop="worker_name" />
      <el-table-column fixed="right" label="操作" width="120">
        <template slot-scope="scope">
          <el-button
            @click.native.prevent="deleteRow(scope.$index)"
            type="danger"
            icon="el-icon-delete"
            size="mini"
            circle
          />
        </template>
      </el-table-column>
    </el-table>
    <el-button type="primary" @click="bind_submit" class="form_submit"> 提交 </el-button>
    <hr />
    <h3>添加项目</h3>
    <el-form inline ref="form">
      <el-form-item label="维修项目">
        <el-select v-model="form.job_name" filterable>
          <el-option v-for="item in job_opts" :key="item" :label="item" :value="item" />
        </el-select>
      </el-form-item>
      <el-form-item label="工时">
        <el-input v-model="form.time" />
      </el-form-item>
      <el-form-item label="维修员工种">
        <el-select v-model="form.worker_name" filterable>
          <el-option v-for="item in worker_opts" :key="item" :label="item" :value="item" />
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="bind_add" size="mini" style="margin: 0 0 0 20px"> 添加 </el-button>
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
      fix_id: "",
      form: {
        job_id: "待分配",
        job_name: "",
        time: "",
        worker_id: "待分配",
        worker_name: "",
      },
      table_data: [],
      job_opts: ["维修车头", "维修车尾"],
      worker_opts: ["机修工", "油漆工"],
    };
  },
  mounted() {
    this.fix_id = this.$route.query.fix_id;
    // this.table_data = api.get_job_list(this.fix_id)
    Axios({
      url: "/job?fix_id=" + this.fix_id,
      method: "get",
    }).then((res) => {
      console.log(JSON.stringify(res.data));
      this.table_data = res.data;
    });
  },
  methods: {
    bind_add() {
      this.table_data.push(this.form);
      this.form = { job_id: "", job_name: "", time: "", worker_id: "", worker_name: "" };
    },
    bind_submit() {
      console.log(JSON.stringify(this.table_data));
      Axios({
        url: "/job?fix_id=" + this.fix_id,
        method: "post",
        data: this.table_data,
      }).then((res) => {
        console.log(res);
      });
    },
    deleteRow(index) {
      console.log(index);
      this.table_data.splice(index, 1);
    },
  },
};
</script>

<style>
.form_submit {
  margin: 20px auto;
  display: flex;
  text-align: center；;
}
</style>