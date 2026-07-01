---
type: protein-evaluation
gene: "ENSG00000283886"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## ENSG00000283886 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | ENSG00000283886 |
| 蛋白名称 | Uncharacterized protein FLJ76381 |
| 蛋白大小 | 153 aa / 17.0 kDa |
| UniProt ID | Q8NFD4 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 153 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=48.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 |  |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |
### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=0 broad=0
- AF pLDDT=48.6 PDB=0
- InterPro: 
- Pfam: 
- PPI deg=0 ChIP: None

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein

### ESM 结构预测补充 (ESMFold Analysis)

**方法**: 使用 Meta ESM Metagenomic Atlas API 对全长蛋白序列进行 ab initio 折叠预测。
**PDB 文件**: `detail/_esm_structures/ENSG00000283886_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.32 |
| pLDDT > 0.9 占比 | 0.0% |
| pLDDT < 0.5 占比 | 100.0% |
| 建模残基数 | 153 |

**与 AlphaFold 对比**:

ESMFold pLDDT (0.32) 低于 AlphaFold pLDDT (48.6) 48.3。

ESMFold 基于进化规模语言模型，对序列空间进行无 MSA 搜索的从头折叠，可作为 AlphaFold 的独立验证和补充。



### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein FLJ76381

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NFD4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 亚细胞定位: https://www.proteinatlas.org/ENSG00000283886-ENSG00000283886/subcellular


### HPA IF 图像

![](https://images.proteinatlas.org/21733/274_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21733/274_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21733/2122_B1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21733/2122_B1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/21733/275_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21733/275_A2_1_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TSPAN11 | STRING | 593 |
