<template>
  <article>
    <div class="desc-item">
      <img :src="item[0].img_url" :alt="item[0].name">
      <div>
        <h1>{{item[0].name}}</h1>
      </div>
    </div>
    <div class="control-item">
      <button @click="clearItem(item[0].id)">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
      <div class="amount-control">
        <button @click="setItemAmount(groupCount(item[0].id)-1, item[0])">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </button>
        <p> {{ groupCount(item[0].id) }} </p>
        <button @click="addItem(1, item[0])">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </button>
      </div>
    </div>
  </article>
</template>

<script>
import { useListStore } from "../../store/ListStore";
import { mapState } from 'pinia';

export default {
  name: 'MyListItem',
  props: ["item"],
  computed: {
    ...mapState(useListStore, ['clearItem', 'groupCount', 'setItemAmount', 'addItem'])
  }
}
</script>

<style scoped>
article {
  @apply flex justify-between items-center m-4 p-2 bg-white shadow-md rounded-xl;
}

.desc-item {
  @apply flex items-center;
}

.desc-item div{
  @apply ml-3;
}

img {
  @apply w-20 h-20 rounded-xl;
}

h1 {
  @apply text-lg font-semibold text-red-400;
}

.control-item {
  @apply flex flex-col justify-between items-end self-stretch;
}

.control-item > button {
  @apply items-end h-auto;
}

.amount-control {
  @apply flex justify-between w-20;
}

.amount-control p{
  @apply text-lg font-semibold;
}

</style>