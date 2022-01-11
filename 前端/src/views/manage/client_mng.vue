<template>
  <div class="app-container">
    <h3>客户列表</h3>
    <el-table :data="table_data" border="true">
      <el-table-column label="客户编号" prop="client_id" width="110" sortable />
      <el-table-column label="客户名称" prop="client_name" sortable />
      <el-table-column
        label="客户类型"
        prop="client_type"
        :filters="[
          { text: '个人', value: '个人' },
          { text: '公司', value: '公司' },
        ]"
        :filter-method="(value, row) => row.client_type === value"
        filter-placement="bottom-end"
      >
        <template slot-scope="scope">
          <el-tag :type="scope.row.client_type === '个人' ? 'primary' : 'success'" disable-transitions>
            {{ scope.row.client_type }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="折扣率(%)" prop="discount" sortable />
      <el-table-column label="联系人" prop="contact" sortable />
      <el-table-column label="手机号" prop="tel" sortable />
      <el-table-column label="拥有车辆">
        <template slot-scope="scope">
          <div v-for="item in scope.row.cars" :key="item.car_id">
            <el-popover trigger="hover" placement="top">
              <p>车型: {{ item.series }}</p>
              <p>颜色: {{ item.color }}</p>
              <p>类型: {{ item.type }}</p>
              <div slot="reference" style="float: left">
                <el-tag size="medium">{{ item.car_id }}</el-tag>
              </div>
            </el-popover>
          </div>
        </template>
      </el-table-column>
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
    this.table_data = api.get_client_list();
  },
  methods: {},
};
</script>