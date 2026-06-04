---
type: protein-evaluation
gene: "EHMT2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EHMT2 — REJECTED (研究热度过高 (PubMed strict=386，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EHMT2 |
| 蛋白名称 | [histone H3]-lysine(9) N-methyltransferase |
| 蛋白大小 | 1267 aa / 138.8 kDa |
| UniProt ID | A0A0G2JK64 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm, Nuclear speckles; UniProt: Chromosome; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1267 aa / 138.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=386 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.2; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.0/180** | |
| **归一化总分** | | | **41.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles | Supported |
| UniProt | Chromosome; Nucleus | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 386 |
| PubMed broad count | 653 |
| 别名(未计入scoring) |  |

**关键文献**:
1. BIX-01294, a pharmacological inhibitor of EHMT2, suppresses retinoblastoma tumorigenesis through MAPK pathway inhibition.. *Eur J Pharmacol*. PMID: 42119769
2. Histone methyltransferase G9a drives vascular smooth muscle cell proliferation and intimal hyperplasia in mice.. *Acta Pharmacol Sin*. PMID: 41663737
3. Mechanism of lncRNA PLACT1 in regulating the proliferation of pancreatic adenocarcinoma cells through the KLF2/KIAA1522 axis.. *Histol Histopathol*. PMID: 41164921
4. The tissue-specific effects of glucose-lowering drug targets on aging mediated through DNA methylation: a multi-omics genetic study.. *BMC Med*. PMID: 42163256
5. Targeting EHMT2 overcomes 5-fluorouracil resistance in colorectal cancer by modulating cell cycle and apoptosis.. *Signal Transduct Target Ther*. PMID: 42144396

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 35.6% |
| 置信残基 (pLDDT 70-90) 占比 | 15.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 42.5% |
| 有序区域 (pLDDT>70) 占比 | 51.0% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 预测质量有限（pLDDT=63.2），有序残基占 51.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EHMT1 | 0.000 | 0.000 | — |
| CBX3 | 0.000 | 0.000 | — |
| HDAC1 | 0.000 | 0.000 | — |
| H3-3B | 0.000 | 0.000 | — |
| DNMT1 | 0.000 | 0.000 | — |
| H3C13 | 0.000 | 0.000 | — |
| H3C12 | 0.000 | 0.000 | — |
| UHRF1 | 0.000 | 0.000 | — |
| H3-4 | 0.000 | 0.000 | — |
| H3-5 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9BT49 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9Y4X4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q96KQ7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8TBB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8N5R6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q5JSZ5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q96JN0 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P62993 | psi-mi:"MI:0081"(peptide array) | pubmed:- |
| uniprotkb:O15084 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:- |
| uniprotkb:Q6MG72 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.2 + PDB: 无 | pLDDT=63.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Chromosome; Nucleus / Nucleoplasm, Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EHMT2 — [histone H3]-lysine(9) N-methyltransferase，研究基础较多，新颖性有限。
2. 蛋白大小1267 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 386 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 386 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A0G2JK64
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204371-EHMT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EHMT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A0G2JK64
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
