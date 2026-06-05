---
type: protein-evaluation
gene: "MYBPH"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MYBPH 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYBPH |
| 蛋白名称 | Myosin-binding protein H |
| 蛋白大小 | 477 aa / 52.0 kDa |
| UniProt ID | Q13203 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nucleoli, Mitochondria; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 477 aa / 52.0 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=66 篇 (≤80→4) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003961, IPR036116, IPR007110, IPR036179, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.0/180** | |
| **归一化总分** | | | **45.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Mitochondria | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- M band (GO:0031430)
- myosin filament (GO:0032982)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 66 |
| PubMed broad count | 80 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. High myosin binding protein H expression predicts poor prognosis in glioma patients.. *Scientific reports*. PMID: 35087137
2. Ascribing novel functions to the sarcomeric protein, myosin binding protein H (MyBPH) in cardiac sarcomere contraction.. *Experimental cell research*. PMID: 25449695
3. MYBPH inhibits vascular smooth muscle cell migration and attenuates neointimal hyperplasia in a rat carotid balloon-injury model.. *Experimental cell research*. PMID: 28800959
4. MYBPH acts as modifier of cardiac hypertrophy in hypertrophic cardiomyopathy (HCM) patients.. *Human genetics*. PMID: 26969327
5. MYBPH, a transcriptional target of TTF-1, inhibits ROCK1, and reduces cell motility and metastasis.. *The EMBO journal*. PMID: 22085929

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003961, IPR036116, IPR007110, IPR036179, IPR013783; Pfam: PF00041, PF07679 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OCA2 | 0.996 | 0.000 | — |
| GLDC | 0.994 | 0.000 | — |
| SLAMF1 | 0.994 | 0.000 | — |
| NECTIN4 | 0.993 | 0.000 | — |
| CD46 | 0.993 | 0.000 | — |
| AMT | 0.984 | 0.000 | — |
| GCSH | 0.957 | 0.000 | — |
| C3 | 0.857 | 0.000 | — |
| TLR2 | 0.836 | 0.000 | — |
| CFH | 0.798 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TTN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| UBL7 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| ZBTB38 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| CAPN3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| PPP1R21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TGS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| WRAP53 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli, Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. MYBPH — Myosin-binding protein H，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小477 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 66 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13203
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133055-MYBPH/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYBPH
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13203
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000133055-MYBPH/subcellular

![](https://images.proteinatlas.org/61383/1397_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/61383/1397_C3_4_red_green.jpg)
![](https://images.proteinatlas.org/61383/1402_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/61383/1402_C3_3_red_green.jpg)
![](https://images.proteinatlas.org/61383/1520_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/61383/1520_B11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13203-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
