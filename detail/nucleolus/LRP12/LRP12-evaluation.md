---
type: protein-evaluation
gene: "LRP12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRP12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRP12 / ST7 |
| 蛋白名称 | Low-density lipoprotein receptor-related protein 12 |
| 蛋白大小 | 859 aa / 95.0 kDa |
| UniProt ID | Q9Y561 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Plasma membrane, Mitochondria; UniProt: Membrane; Membrane, coated pit |
| 蛋白大小 | 8/10 | ×1 | 8 | 859 aa / 95.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=46 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000859, IPR036055, IPR023415, IPR002172, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Plasma membrane, Mitochondria | Approved |
| UniProt | Membrane; Membrane, coated pit | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- clathrin-coated pit (GO:0005905)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 46 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ST7 |

**关键文献**:
1. Oculopharyngodistal myopathy.. *Current opinion in neurology*. PMID: 35942670
2. GGC Repeat Expansion of RILPL1 is Associated with Oculopharyngodistal Myopathy.. *Annals of neurology*. PMID: 35700120
3. CGG repeat expansions in Charcot-Marie-Tooth disease: insights from the 100 000 Genomes Project.. *Journal of neurology, neurosurgery, and psychiatry*. PMID: 40645757
4. LRP12 promotes gastric cancer progression through AKT/mTOR signaling and M2 macrophage-mediated immunosuppression.. *Scientific reports*. PMID: 41276539
5. The GGC repeat expansion in NOTCH2NLC is associated with oculopharyngodistal myopathy type 3.. *Brain : a journal of neurology*. PMID: 33693509

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.5 |
| 高置信度残基 (pLDDT>90) 占比 | 12.2% |
| 置信残基 (pLDDT 70-90) 占比 | 38.5% |
| 中等置信 (pLDDT 50-70) 占比 | 13.7% |
| 低置信 (pLDDT<50) 占比 | 35.5% |
| 有序区域 (pLDDT>70) 占比 | 50.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.5），有序残基占 50.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000859, IPR036055, IPR023415, IPR002172, IPR035914; Pfam: PF00431, PF00057 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOTCH2NLC | 0.722 | 0.000 | — |
| NOTCH2NLA | 0.609 | 0.000 | — |
| HSPG2 | 0.577 | 0.300 | — |
| AGRN | 0.575 | 0.300 | — |
| NBPF19 | 0.546 | 0.000 | — |
| NBPF19-2 | 0.545 | 0.000 | — |
| GIPC1 | 0.529 | 0.045 | — |
| LRP11 | 0.490 | 0.000 | — |
| APOE | 0.477 | 0.000 | — |
| APOB | 0.463 | 0.061 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACTN2 | psi-mi:"MI:0018"(two hybrid) | pubmed:12809483 |
| MYOT | psi-mi:"MI:0018"(two hybrid) | pubmed:12809483 |
| SNAPIN | psi-mi:"MI:0018"(two hybrid) | pubmed:12809483 |
| RACK1 | psi-mi:"MI:0018"(two hybrid) | pubmed:12809483 |
| NMRK2 | psi-mi:"MI:0018"(two hybrid) | pubmed:12809483 |
| ZFYVE9 | psi-mi:"MI:0018"(two hybrid) | pubmed:12809483 |
| PSG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IL17RC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KIR3DL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMED6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.5 + PDB: 无 | pLDDT=62.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Membrane, coated pit / Nucleoli fibrillar center, Plasma membrane, Mitoch | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRP12 — Low-density lipoprotein receptor-related protein 12，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小859 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 46 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y561
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147650-LRP12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRP12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y561
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000147650-LRP12/subcellular

![](https://images.proteinatlas.org/17245/138_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17245/138_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17245/139_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17245/139_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17245/166_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17245/166_D11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y561-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y561 |
| SMART | SM00042;SM00192; |
| UniProt Domain [FT] | DOMAIN 47..159; /note="CUB 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00059"; DOMAIN 165..201; /note="LDL-receptor class A 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 214..255; /note="LDL-receptor class A 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 259..372; /note="CUB 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00059"; DOMAIN 374..411; /note="LDL-receptor class A 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 412..449; /note="LDL-receptor class A 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124"; DOMAIN 450..486; /note="LDL-receptor class A 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00124" |
| InterPro | IPR000859;IPR036055;IPR023415;IPR002172;IPR035914; |
| Pfam | PF00431;PF00057; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000147650-LRP12/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NMRK2 | Intact | false |
| RACK1 | Intact | false |
| ZDHHC15 | Biogrid | false |
| ZFYVE9 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
