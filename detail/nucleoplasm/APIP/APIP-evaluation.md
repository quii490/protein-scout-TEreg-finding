---
type: protein-evaluation
gene: "APIP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## APIP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | APIP |
| 蛋白名称 | Methylthioribulose-1-phosphate dehydratase |
| 蛋白大小 | 242 aa / 27.1 kDa |
| UniProt ID | Q96GX9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 242 aa / 27.1 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.9; PDB: 4M6R |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001303, IPR036409, IPR017714, IPR027514; Pfam:  |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107.0/180** | |
| **归一化总分** | | | **59.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 101 |
| 别名(未计入scoring) |  |

**关键文献**:
1. APIP regulates the priming of canonical NLRP3 and non-canonical Caspase-11/4 inflammasomes by binding to TRAF6.. *Nature communications*. PMID: 41339302
2. APIP regulated by YAP propels methionine cycle and metastasis in head and neck squamous cell carcinoma.. *Cancer letters*. PMID: 38423248
3. Cardioprotective role of APIP in myocardial infarction through ADORA2B.. *Cell death & disease*. PMID: 31263105
4. Apaf-1 interacting protein, a new target of microRNA-146a-3p, promotes prostate cancer cell development via the ERK1/2 pathway.. *Cell biology international*. PMID: 35293661
5. Clinical pathological significance and biological functions of APIP in hepatocellular carcinoma.. *Cancer cell international*. PMID: 41126213

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.9 |
| 高置信度残基 (pLDDT>90) 占比 | 88.8% |
| 置信残基 (pLDDT 70-90) 占比 | 3.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.4% |
| 低置信 (pLDDT<50) 占比 | 7.0% |
| 有序区域 (pLDDT>70) 占比 | 92.5% |
| 可用 PDB 条目 | 4M6R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.9，有序区 92.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001303, IPR036409, IPR017714, IPR027514; Pfam: PF00596 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ENOPH1 | 0.999 | 0.000 | — |
| MRI1 | 0.992 | 0.000 | — |
| APAF1 | 0.969 | 0.292 | — |
| ADI1 | 0.959 | 0.000 | — |
| XYLB | 0.793 | 0.000 | — |
| CASP9 | 0.789 | 0.000 | — |
| CYCS | 0.762 | 0.000 | — |
| TPI1 | 0.757 | 0.000 | — |
| MTAP | 0.743 | 0.000 | — |
| EHF | 0.667 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A8K9D3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NUDT18 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TRAF2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| VPS25 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LNX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| wbtM | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| VIM | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NIF3L1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| A0A0H2W437 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.9 + PDB: 4M6R | pLDDT=92.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. APIP — Methylthioribulose-1-phosphate dehydratase，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小242 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96GX9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149089-APIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=APIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96GX9
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:59:01

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000149089-APIP/subcellular

![](https://images.proteinatlas.org/21188/1158_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/21188/1158_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/21188/1210_H6_3_red_green.jpg)
![](https://images.proteinatlas.org/21188/1210_H6_4_red_green.jpg)
![](https://images.proteinatlas.org/21188/1401_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/21188/1401_E11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96GX9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
