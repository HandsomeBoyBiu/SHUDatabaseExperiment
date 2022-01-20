<template>
  <div class="app-container">
    <h3>维修委托列表</h3>
    <el-table :data="table_data" border=true>
      <el-table-column label="委托编号" prop="fix_id" sortable />
      <el-table-column label="车牌号" prop="car_id" sortable />
      <el-table-column label="客户号" prop="client_id" sortable />
      <el-table-column
        label="维修类型"
        prop="priority"
        :filters="[
          { text: '加急', value: '加急' },
          { text: '普通', value: '普通' },
        ]"
        :filter-method="(value, row) => row.priority === value"
      >
        <template slot-scope="scope">
          <el-tag :type="scope.row.priority === '普通' ? 'success' : 'danger'" disable-transitions>
            {{ scope.row.priority }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="作业分类" prop="type" sortable />
      <el-table-column label="结算方式" prop="pay" sortable />
      <el-table-column label="进厂时间" prop="in_time" sortable />
      <el-table-column label="业务员" prop="clerk_name" sortable />
      <el-table-column label="业务员编号" prop="clerk_id" sortable />
      <el-table-column label="预计完工时间" prop="est_time" sortable />
      <el-table-column label="故障描述" prop="describe" />
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            @click.native.prevent="to_job(scope.row.fix_id)"
            type="success"
            size="small"
            plain
          >管理派工单</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import api from "@/utils/api";
export default {
  data() {
    return {
      table_data: [],
    };
  },
  mounted() {
    this.table_data = api.get_fix_list();
  },
  methods: {
    to_job(fix_id){
      // console.log(fix_id)
      this.$router.push({path:'/reg/job_reg',query:{fix_id}})
    }

  },
};
</script>