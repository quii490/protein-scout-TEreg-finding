---
type: protein-evaluation
gene: "DUSP10"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DUSP10 — REJECTED (研究热度过高 (PubMed strict=102，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP10 / MKP5 |
| 蛋白名称 | Dual specificity protein phosphatase 10 |
| 蛋白大小 | 482 aa / 52.6 kDa |
| UniProt ID | Q9Y6W6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 482 aa / 52.6 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=102 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.2; PDB: 1ZZW, 2OUC, 2OUD, 3TG1, 6MC1, 7U4O, 7U4R |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000340, IPR008343, IPR029021, IPR001763, IPR036 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 102 |
| PubMed broad count | 168 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MKP5 |

**关键文献**:
1. BRCC3-Mediated NLRP3 Deubiquitylation Promotes Inflammasome Activation and Atherosclerosis in Tet2 Clonal Hematopoiesis.. *Circulation*. PMID: 37781816
2. A Spanish-Portuguese GWAS of progressive supranuclear palsy reveals a novel risk locus in NFASC.. *European journal of human genetics : EJHG*. PMID: 40379966
3. DUSP10 is a novel immune-related biomarker connected with survival and cellular proliferation in lower-grade glioma.. *Aging*. PMID: 37387540
4. The Dual-Specificity Phosphatase 10 (DUSP10): Its Role in Cancer, Inflammation, and Immunity.. *International journal of molecular sciences*. PMID: 30939861
5. DUSP10 upregulation is a poor prognosticator and promotes cell proliferation and migration in glioma.. *Frontiers in oncology*. PMID: 36713584

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.2 |
| 高置信度残基 (pLDDT>90) 占比 | 35.5% |
| 置信残基 (pLDDT 70-90) 占比 | 21.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 32.6% |
| 有序区域 (pLDDT>70) 占比 | 56.5% |
| 可用 PDB 条目 | 1ZZW, 2OUC, 2OUD, 3TG1, 6MC1, 7U4O, 7U4R, 7UMU, 7UMV, 7UN0 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.2），有序残基占 56.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000340, IPR008343, IPR029021, IPR001763, IPR036873; Pfam: PF00782, PF00581 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAPK8 | 0.993 | 0.705 | — |
| MAPK14 | 0.989 | 0.818 | — |
| MAPK9 | 0.979 | 0.690 | — |
| MAPK11 | 0.908 | 0.444 | — |
| MAPK12 | 0.886 | 0.401 | — |
| MAPK13 | 0.883 | 0.401 | — |
| JKAMP | 0.870 | 0.000 | — |
| MAPK1 | 0.813 | 0.267 | — |
| MAPK3 | 0.811 | 0.243 | — |
| JUN | 0.587 | 0.111 | — |

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
| 三维结构 | AlphaFold pLDDT=69.2 + PDB: 1ZZW, 2OUC, 2OUD, 3TG1, 6MC1,  | pLDDT=69.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DUSP10 — Dual specificity protein phosphatase 10，有一定研究基础，但仍存在niche空间。
2. 蛋白大小482 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 102 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=69.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 102 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6W6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143507-DUSP10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6W6
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:20:36

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000143507-DUSP10/subcellular

![](https://images.proteinatlas.org/16758/278_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/16758/278_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/16758/279_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/16758/279_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/16758/280_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/16758/280_A4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
