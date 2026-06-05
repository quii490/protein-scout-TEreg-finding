---
type: protein-evaluation
gene: "SEPTIN5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SEPTIN5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SEPTIN5 / PNUTL1, SEPT5 |
| 蛋白名称 | Septin-5 |
| 蛋白大小 | 369 aa / 42.8 kDa |
| UniProt ID | Q99719 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Actin filaments, Cytosol; UniProt: Cytoplasm; Cytoplasm, cytoskeleton |
| 蛋白大小 | 10/10 | ×1 | 10 | 369 aa / 42.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=77.5; PDB: 6WCU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR030379, IPR027417, IPR016491; Pfam: PF00735 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Actin filaments, Cytosol | Approved |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell division site (GO:0032153)
- microtubule cytoskeleton (GO:0015630)
- plasma membrane (GO:0005886)
- septin complex (GO:0031105)
- septin ring (GO:0005940)
- synaptic vesicle (GO:0008021)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 108 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PNUTL1, SEPT5 |

**关键文献**:
1. Autoimmune Movement Disorders.. *Continuum (Minneapolis, Minn.)*. PMID: 39088289
2. Autoimmune Vestibulocerebellar Syndromes.. *Seminars in neurology*. PMID: 31958862
3. Presynaptic Vesicle Protein SEPTIN5 Regulates the Degradation of APP C-Terminal Fragments and the Levels of Aβ.. *Cells*. PMID: 33203136
4. Autoimmune septin-5 cerebellar ataxia.. *Neurology(R) neuroimmunology & neuroinflammation*. PMID: 29998156
5. S327 phosphorylation of the presynaptic protein SEPTIN5 increases in the early stages of neurofibrillary pathology and alters the functionality of SEPTIN5.. *Neurobiology of disease*. PMID: 34954322

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.5 |
| 高置信度残基 (pLDDT>90) 占比 | 18.7% |
| 置信残基 (pLDDT 70-90) 占比 | 59.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 11.4% |
| 有序区域 (pLDDT>70) 占比 | 78.3% |
| 可用 PDB 条目 | 6WCU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=77.5，有序区 78.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030379, IPR027417, IPR016491; Pfam: PF00735 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SEPTIN11 | 0.997 | 0.936 | — |
| SEPTIN6 | 0.996 | 0.925 | — |
| SEPTIN7 | 0.993 | 0.898 | — |
| PRKN | 0.991 | 0.785 | — |
| SEPTIN8 | 0.990 | 0.923 | — |
| SEPTIN3 | 0.989 | 0.898 | — |
| SEPTIN12 | 0.988 | 0.921 | — |
| SEPTIN4 | 0.986 | 0.230 | — |
| SEPTIN10 | 0.975 | 0.931 | — |
| SEPTIN2 | 0.973 | 0.895 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.5 + PDB: 6WCU | pLDDT=77.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton / Nucleoplasm, Actin filaments, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SEPTIN5 — Septin-5，非常新颖，仅有少数基础研究。
2. 蛋白大小369 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99719
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184702-SEPTIN5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SEPTIN5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99719
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000184702-SEPTIN5/subcellular

![](https://images.proteinatlas.org/29095/831_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29095/831_C11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/29095/882_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29095/882_C11_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99719-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
