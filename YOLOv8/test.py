import torch
print('CUDA版本:',torch.version.cuda)
print('Pytorch版本:',torch.__version__)
print('顯示卡是否可用:','可用' if(torch.cuda.is_available()) else '不可用')
print('顯示卡數量:',torch.cuda.device_count())
print('是否支援BF16數字格式:','支援' if (torch.cuda.is_bf16_supported()) else '不支援')
print('當前顯示卡型號:',torch.cuda.get_device_name())
print('當前顯示卡的CUDA算力:',
      ())
print('當前顯示卡的總視訊記憶體:',torch.cuda.get_device_properties(0).total_memory/1024/1024/1024,'GB')
print('是否支援TensorCore:','支援' if (torch.cuda.get_device_properties(0).major >= 7) else '不支援')
print('當前顯示卡的視訊記憶體使用率:',torch.cuda.memory_allocated(0)/torch.cuda.get_device_properties(0).total_memory*100,'%')