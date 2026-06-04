---
type: protein-evaluation
gene: "SUV39H2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SUV39H2 — REJECTED (研究热度过高 (PubMed strict=101，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUV39H2 / KMT1B |
| 蛋白名称 | Histone-lysine N-methyltransferase SUV39H2 |
| 蛋白大小 | 410 aa / 46.7 kDa |
| UniProt ID | Q9H5I1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; UniProt: Nucleus; Chromosome, centromere |
| 蛋白大小 | 10/10 | ×1 | 10 | 410 aa / 46.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=101 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=89.1; PDB: 2R3A, 6P0R |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016197, IPR000953, IPR023780, IPR023779, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria | Uncertain |
| UniProt | Nucleus; Chromosome, centromere | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome, centromeric region (GO:0000775)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 101 |
| PubMed broad count | 171 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KMT1B |

**关键文献**:
1. Establishment of H3K9-methylated heterochromatin and its functions in tissue differentiation and maintenance.. *Nature reviews. Molecular cell biology*. PMID: 35562425
2. Lysine methylation of PPP1CA by the methyltransferase SUV39H2 disrupts TFEB-dependent autophagy and promotes intervertebral disc degeneration.. *Cell death and differentiation*. PMID: 37605006
3. Distinct H3K9me3 heterochromatin maintenance dynamics govern different gene programmes and repeats in pluripotent cells.. *Nature cell biology*. PMID: 39482359
4. Structure, Activity and Function of the Suv39h1 and Suv39h2 Protein Lysine Methyltransferases.. *Life (Basel, Switzerland)*. PMID: 34357075
5. SUV39H2 controls trophoblast stem cell fate.. *Biochimica et biophysica acta. General subjects*. PMID: 33556426

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.1 |
| 高置信度残基 (pLDDT>90) 占比 | 72.4% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 6.6% |
| 有序区域 (pLDDT>70) 占比 | 89.2% |
| 可用 PDB 条目 | 2R3A, 6P0R |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2R3A, 6P0R）+ AlphaFold高质量预测（pLDDT=89.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016197, IPR000953, IPR023780, IPR023779, IPR011381; Pfam: PF00385, PF05033, PF00856 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CBX1 | 0.915 | 0.852 | — |
| EIF2S3 | 0.905 | 0.093 | — |
| EIF2S3B | 0.902 | 0.093 | — |
| CBX5 | 0.898 | 0.818 | — |
| H3C12 | 0.838 | 0.310 | — |
| H3C13 | 0.837 | 0.310 | — |
| CBX3 | 0.827 | 0.694 | — |
| CAMKMT | 0.812 | 0.000 | — |
| DNMT1 | 0.770 | 0.053 | — |
| H3-5 | 0.741 | 0.310 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q9JLP7 | psi-mi:"MI:0516"(methyltransferase radiometric ass | pubmed:10949293 |
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBE2V2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CGGBP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| grxC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.1 + PDB: 2R3A, 6P0R | pLDDT=89.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere / Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SUV39H2 — Histone-lysine N-methyltransferase SUV39H2，研究基础较多，新颖性有限。
2. 蛋白大小410 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 101 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 101 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H5I1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152455-SUV39H2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUV39H2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H5I1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
