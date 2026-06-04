---
type: protein-evaluation
gene: "TBK1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TBK1 — REJECTED (研究热度过高 (PubMed strict=1896，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBK1 / NAK |
| 蛋白名称 | Serine/threonine-protein kinase TBK1 |
| 蛋白大小 | 729 aa / 83.6 kDa |
| UniProt ID | Q9UHD2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 729 aa / 83.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1896 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.7; PDB: 4EFO, 4EUT, 4EUU, 4IM0, 4IM2, 4IM3, 4IW0 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051180, IPR011009, IPR000719, IPR017441, IPR041 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Enhanced |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- serine/threonine protein kinase complex (GO:1902554)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1896 |
| PubMed broad count | 3201 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NAK |

**关键文献**:
1. Targeting TBK1 to overcome resistance to cancer immunotherapy.. *Nature*. PMID: 36634707
2. SIRT5 safeguards against primate skeletal muscle ageing via desuccinylation of TBK1.. *Nature metabolism*. PMID: 40087407
3. Mutant p53 suppresses innate immune signaling to promote tumorigenesis.. *Cancer cell*. PMID: 33545063
4. TBK1 and IKKε prevent TNF-induced cell death by RIPK1 phosphorylation.. *Nature cell biology*. PMID: 30420664
5. Haploinsufficiency of TBK1 causes familial ALS and fronto-temporal dementia.. *Nature neuroscience*. PMID: 25803835

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.7 |
| 高置信度残基 (pLDDT>90) 占比 | 71.6% |
| 置信残基 (pLDDT 70-90) 占比 | 19.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 3.6% |
| 有序区域 (pLDDT>70) 占比 | 90.9% |
| 可用 PDB 条目 | 4EFO, 4EUT, 4EUU, 4IM0, 4IM2, 4IM3, 4IW0, 4IWO, 4IWP, 4IWQ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4EFO, 4EUT, 4EUU, 4IM0, 4IM2, 4IM3, 4IW0, 4IWO, 4IWP, 4IWQ）+ AlphaFold极高置信度预测（pLDDT=89.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051180, IPR011009, IPR000719, IPR017441, IPR041309; Pfam: PF00069, PF18394, PF18396 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IRF3 | 0.999 | 0.927 | — |
| TANK | 0.999 | 0.994 | — |
| OPTN | 0.999 | 0.991 | — |
| TBKBP1 | 0.999 | 0.994 | — |
| IKBKE | 0.999 | 0.994 | — |
| STING1 | 0.999 | 0.991 | — |
| DDX3X | 0.999 | 0.306 | — |
| AZI2 | 0.999 | 0.999 | — |
| TRAF3 | 0.999 | 0.994 | — |
| MAVS | 0.999 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| P | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:20089657|imex:IM-28090 |
| ENSP00000498995.1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| US11 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| VP35 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.7 + PDB: 4EFO, 4EUT, 4EUU, 4IM0, 4IM2,  | pLDDT=89.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. TBK1 — Serine/threonine-protein kinase TBK1，研究基础较多，新颖性有限。
2. 蛋白大小729 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1896 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1896 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHD2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183735-TBK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHD2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
