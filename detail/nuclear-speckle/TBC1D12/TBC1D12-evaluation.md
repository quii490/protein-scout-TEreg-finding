---
type: protein-evaluation
gene: "TBC1D12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TBC1D12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBC1D12 / KIAA0608 |
| 蛋白名称 | TBC1 domain family member 12 |
| 蛋白大小 | 775 aa / 85.6 kDa |
| UniProt ID | O60347 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear speckles; UniProt: Endosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 775 aa / 85.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000195, IPR035969, IPR050302; Pfam: PF00566 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles | Approved |
| UniProt | Endosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- autophagosome (GO:0005776)
- recycling endosome (GO:0055037)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0608 |

**关键文献**:
1. Identification and validation of a signature based on macrophage cell marker genes to predict recurrent miscarriage by integrated analysis of single-cell and bulk RNA-sequencing.. *Frontiers in immunology*. PMID: 36439123
2. Adaptations to climate-mediated selective pressures in sheep.. *Molecular biology and evolution*. PMID: 25249477
3. In silico approach uncovers the shared genetic landscape of type 2 diabetes mellitus and asthenozoospermia.. *Systems biology in reproductive medicine*. PMID: 39292564
4. Identification of the BRAF V600E mutation in gastroenteropancreatic neuroendocrine tumors.. *Oncotarget*. PMID: 26684240
5. A study of gene expression by RNA-seq in patients with prostate cancer and in patients with Parkinson disease: an example of inverse comorbidity.. *Molecular biology reports*. PMID: 34628580

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.9 |
| 高置信度残基 (pLDDT>90) 占比 | 36.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 49.3% |
| 有序区域 (pLDDT>70) 占比 | 44.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.9），有序残基占 44.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000195, IPR035969, IPR050302; Pfam: PF00566 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 1
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.9 + PDB: 无 | pLDDT=62.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endosome / Nucleoplasm, Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 0 + 1 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TBC1D12 — TBC1 domain family member 12，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小775 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60347
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108239-TBC1D12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBC1D12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60347
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000108239-TBC1D12/subcellular

![](https://images.proteinatlas.org/38277/431_G8_3_red_green.jpg)
![](https://images.proteinatlas.org/38277/431_G8_4_red_green.jpg)
![](https://images.proteinatlas.org/38277/437_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/38277/437_G8_3_red_green.jpg)
![](https://images.proteinatlas.org/38277/443_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/38277/443_G8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60347-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
