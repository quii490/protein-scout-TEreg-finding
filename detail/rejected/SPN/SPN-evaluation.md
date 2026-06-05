---
type: protein-evaluation
gene: "SPN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SPN — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3); 研究热度过高 (PubMed strict=507，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPN / CD43 |
| 蛋白名称 | Leukosialin |
| 蛋白大小 | 400 aa / 40.3 kDa |
| UniProt ID | P16150 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: Plasma membrane; UniProt: Membrane; Cell projection, microvillus; Cell projection, uro |
| 蛋白大小 | 10/10 | ×1 | 10 | 400 aa / 40.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=507 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038829 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.0/180** | |
| **归一化总分** | | | **35.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Approved |
| UniProt | Membrane; Cell projection, microvillus; Cell projection, uropodium; Nucleus; Nucleus, PML body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- basement membrane (GO:0005604)
- cell surface (GO:0009986)
- external side of plasma membrane (GO:0009897)
- extracellular exosome (GO:0070062)
- extracellular space (GO:0005615)
- membrane (GO:0016020)
- microvillus (GO:0005902)
- plasma membrane (GO:0005886)

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 507 |
| PubMed broad count | 3905 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CD43 |

**关键文献**:
1. Guidelines for the provision of nutrition support therapy in the adult critically ill patient: The American Society for Parenteral and Enteral Nutrition.. *JPEN. Journal of parenteral and enteral nutrition*. PMID: 34784064
2. Differentiation-related genes in tumor-associated macrophages as potential prognostic biomarkers in non-small cell lung cancer.. *Frontiers in immunology*. PMID: 36969247
3. Locomotion activates PKA through dopamine and adenosine in striatal neurons.. *Nature*. PMID: 36352228
4. SPINOPHILIN: A multiplayer tumor suppressor.. *Genes & diseases*. PMID: 37013033
5. Endometriosis: From Genes to Global Burden.. *International journal of molecular sciences*. PMID: 41516028

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.3 |
| 高置信度残基 (pLDDT>90) 占比 | 4.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.0% |
| 中等置信 (pLDDT 50-70) 占比 | 45.2% |
| 低置信 (pLDDT<50) 占比 | 45.8% |
| 有序区域 (pLDDT>70) 占比 | 9.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.3），有序残基占 9.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038829 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RDX | 0.995 | 0.900 | — |
| PTPRC | 0.993 | 0.000 | — |
| SIGLEC1 | 0.990 | 0.126 | — |
| SELE | 0.988 | 0.099 | — |
| ICAM1 | 0.977 | 0.000 | — |
| EZR | 0.974 | 0.292 | — |
| SELPLG | 0.972 | 0.074 | — |
| MSN | 0.970 | 0.510 | — |
| BSG | 0.953 | 0.087 | — |
| CD5 | 0.940 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Vha55 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Ir76b | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Dmel\CG14441 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| sog | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| "BG:DS03323.1" | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Dap160 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Dmel\CG16711 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Xpc | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Dmel\CG18368 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| EBI-9933576 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.3 + PDB: 无 | pLDDT=53.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Cell projection, microvillus; Cell proje / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SPN — Leukosialin，研究基础较多，新颖性有限。
2. 蛋白大小400 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 507 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=53.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P16150
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197471-SPN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P16150
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000197471-SPN/subcellular

![](https://images.proteinatlas.org/55244/1770_H9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/55244/1770_H9_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/55244/1817_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55244/1817_E10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55244/1869_G11_25_cr5b741889739e5_blue_red_green.jpg)
![](https://images.proteinatlas.org/55244/1869_G11_27_cr5b74188972a77_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P16150-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
