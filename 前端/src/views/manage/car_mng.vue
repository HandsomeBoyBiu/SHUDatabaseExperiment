<template>
  <div class="app-container">
    <h3>车辆列表</h3>
    <el-table :data="table_data" border="true">
      <el-table-column label="车牌号" prop="car_id" sortable />
      <el-table-column label="颜色" prop="color" sortable />
      <el-table-column label="车型" prop="series" sortable />
      <el-table-column label="车辆类别" prop="type" sortable />

      <!--       <el-table-column fixed="right" label="操作" >
        <template slot-scope="scope">
          <el-button
            @click.native.prevent="deleteRow(scope.$index)"
            type="danger"
            icon="el-icon-delete"
            size="mini"
            circle
          />
        </template>
      </el-table-column> -->
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
    this.table_data = api.get_car_list();
  },
  methods: {},
};
</script>