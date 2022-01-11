<template>
  <div class="app-container">
    <h3>添加项目</h3>
    <el-form inline ref="form">
      <el-form-item label="维修项目编号">
        <el-input size="mini" v-model="form.fix_id" />
      </el-form-item>
      <el-form-item label="维修项目">
        <el-input size="mini" v-model="form.fix_name" />
      </el-form-item>
      <el-form-item label="工时">
        <el-input size="mini" v-model="form.time" />
      </el-form-item>
      <el-form-item label="维修员编号">
        <el-input size="mini" v-model="form.worker_id" />
      </el-form-item>
      <el-form-item label="维修员工种">
        <el-input size="mini" v-model="form.worker_name" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="bind_add" size="mini" style="margin: 0 0 0 20px"> 添加 </el-button>
      </el-form-item>
    </el-form>

    <hr />
    <h3>派工单</h3>
    <el-table :data="table_data">
      <el-table-column label="维修项目编号" prop="fix_id" />
      <el-table-column label="维修项目" prop="fix_name" />
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
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        fix_id: "",
        fix_name: "",
        time: "",
        worker_id: "",
        worker_name: "",
      },
      table_data: [],
    };
  },
  mounted() {},
  methods: {
    bind_add() {
      this.table_data.push(this.form);
      this.form = { fix_id: "", fix_name: "", time: "", worker_id: "", worker_name: "" };
    },
    bind_submit(){
      console.log(JSON.stringify(this.table_data))
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