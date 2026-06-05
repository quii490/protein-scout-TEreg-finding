---
type: protein-evaluation
gene: "GLRX3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GLRX3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLRX3 / PICOT, TXNL2 |
| 蛋白名称 | Glutaredoxin-3 |
| 蛋白大小 | 335 aa / 37.4 kDa |
| UniProt ID | O76003 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytosol; Cytoplasm, cell cortex; Cytoplasm, myofi |
| 蛋白大小 | 10/10 | ×1 | 10 | 335 aa / 37.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.6; PDB: 2DIY, 2WZ9, 2YAN, 3ZYW |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002109, IPR033658, IPR004480, IPR036249, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytosol; Cytoplasm, cell cortex; Cytoplasm, myofibril, sarcomere, Z line | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- iron-sulfur cluster assembly complex (GO:1990229)
- nucleus (GO:0005634)
- Z disc (GO:0030018)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PICOT, TXNL2 |

**关键文献**:
1. Generation of Domain-Specific Monoclonal Antibodies Against Human Glutaredoxin3.. *Monoclonal antibodies in immunodiagnosis and immunotherapy*. PMID: 27923109
2. Human glutaredoxin 3 forms [2Fe-2S]-bridged complexes with human BolA2.. *Biochemistry*. PMID: 22309771
3. LncRNA FGF7-5 and lncRNA GLRX3 together inhibits the formation of carotid plaque via regulating the miR-2681-5p/ERCC4 axis in atherosclerosis.. *Cell cycle (Georgetown, Tex.)*. PMID: 36071684
4. A Glutaredoxin·BolA Complex Serves as an Iron-Sulfur Cluster Chaperone for the Cytosolic Cluster Assembly Machinery.. *The Journal of biological chemistry*. PMID: 27519415
5. [Proliferation and apoptosis of lung cancer cells regulated by gultaredoxin 3].. *Zhonghua zhong liu za zhi [Chinese journal of oncology]*. PMID: 29860757

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.6 |
| 高置信度残基 (pLDDT>90) 占比 | 71.3% |
| 置信残基 (pLDDT 70-90) 占比 | 20.9% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 6.0% |
| 有序区域 (pLDDT>70) 占比 | 92.2% |
| 可用 PDB 条目 | 2DIY, 2WZ9, 2YAN, 3ZYW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2DIY, 2WZ9, 2YAN, 3ZYW）+ AlphaFold高质量预测（pLDDT=88.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002109, IPR033658, IPR004480, IPR036249, IPR013766; Pfam: PF00462, PF00085 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BOLA2B | 0.998 | 0.931 | — |
| BOLA2 | 0.995 | 0.786 | — |
| CIAPIN1 | 0.995 | 0.976 | — |
| BOLA1 | 0.992 | 0.936 | — |
| BOLA3 | 0.955 | 0.664 | — |
| PRKCQ | 0.922 | 0.292 | — |
| GLRX | 0.888 | 0.100 | — |
| ISCU | 0.883 | 0.099 | — |
| ACO1 | 0.883 | 0.000 | — |
| GLRX2 | 0.879 | 0.100 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000435445.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| CIAPIN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRTAP4-12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NADK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PRKCQ | psi-mi:"MI:0018"(two hybrid) | pubmed:10636891 |
| ADAMTSL4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PLSCR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FRA10AC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HEXD | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TNIK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.6 + PDB: 2DIY, 2WZ9, 2YAN, 3ZYW | pLDDT=88.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Cytoplasm, cell cortex; Cytopl / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GLRX3 — Glutaredoxin-3，非常新颖，仅有少数基础研究。
2. 蛋白大小335 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O76003
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108010-GLRX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLRX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O76003
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O76003-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
