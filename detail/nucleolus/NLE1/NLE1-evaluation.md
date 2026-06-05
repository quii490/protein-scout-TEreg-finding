---
type: protein-evaluation
gene: "NLE1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NLE1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NLE1 |
| 蛋白名称 | Notchless protein homolog 1 |
| 蛋白大小 | 485 aa / 53.3 kDa |
| UniProt ID | Q9NVX2 |
| 数据采集时间 | 2026-06-03 23:47:29 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | x1 | 10 | 485 aa / 53.3 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=14 篇 (<= 20 -> 10) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=93.7; PDB: 6WAJ, 8FL0, 8FL2, 8FL3, 8FL4, 8INK, |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR012972, IPR015943, IPR001632, IPR020472, I |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **150.5/180** | |
| **归一化总分** | | | **83.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 46 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Targeting glioblastoma with a brain-penetrant drug that impairs brain tumor stem cells via NLE1-Notch1 complex.. *Stem cell reports*. PMID: 39423824
2. WD40 Protein NLE1 as a Novel Diagnostic Biomarker Promoting Hepatocellular Carcinoma Proliferation.. *Clinical Medicine Insights. Oncology*. PMID: 40625398
3. SMAD4 Loss Induces c-MYC-Mediated NLE1 Upregulation to Support Protein Biosynthesis, Colorectal Cancer Growth, and Metastasis.. *Cancer research*. PMID: 36219392
4. Developmental changes in Notch1 and NLE1 expression in a genetic model of absence epilepsy.. *Brain structure & function*. PMID: 28210849
5. The AT4 receptor agonist [Nle1]-angiotensin IV reduces mechanically induced immediate-early gene expression in the isolated rabbit heart.. *Regulatory peptides*. PMID: 9350976

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.7 |
| 高置信度残基 (pLDDT>90) 占比 | 85.6% |
| 置信残基 (pLDDT 70-90) 占比 | 11.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.4% |
| 低置信 (pLDDT<50) 占比 | 2.3% |
| 有序区域 (pLDDT>70) 占比 | 97.4% |
| 可用 PDB 条目 | 6WAJ, 8FL0, 8FL2, 8FL3, 8FL4, 8INK, 8IPD, 8IPX, 8IPY, 8IR1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6WAJ, 8FL0, 8FL2, 8FL3, 8FL4, 8INK, 8IPD, 8IPX, 8IPY, 8IR1）+ AlphaFold极高置信度预测（pLDDT=93.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012972, IPR015943, IPR001632, IPR020472, IPR019775; Pfam: PF08154, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| IGHMBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLEKHO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPL15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPL18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RBM4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MECP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NSA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.7 + PDB: 6WAJ, 8FL0, 8FL2, 8FL3, 8FL4,  | pLDDT=93.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. NLE1 -- Notchless protein homolog 1，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小485 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVX2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000073536-NLE1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NLE1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVX2
- STRING: https://string-db.org/network/9606.NLE1
- Packet data timestamp: 2026-06-03 23:47:29

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000073536-NLE1/subcellular

![](https://images.proteinatlas.org/18807/115_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/18807/115_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/18807/116_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/18807/116_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/18807/117_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/18807/117_C2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NVX2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
