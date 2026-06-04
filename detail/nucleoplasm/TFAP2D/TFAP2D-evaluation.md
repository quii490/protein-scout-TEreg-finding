---
type: protein-evaluation
gene: "TFAP2D"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TFAP2D 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TFAP2D / TFAP2BL1 |
| 蛋白名称 | Transcription factor AP-2-delta |
| 蛋白大小 | 452 aa / 49.6 kDa |
| UniProt ID | Q7Z6R9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Golgi apparatus, Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 452 aa / 49.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004979, IPR013854; Pfam: PF03299 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Vesicles | Uncertain |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TFAP2BL1 |

**关键文献**:
1. Specification of claustro-amygdalar and palaeocortical neurons and circuits.. *Nature*. PMID: 39814878
2. Brain region-dependent gene networks associated with selective breeding for increased voluntary wheel-running behavior.. *PloS one*. PMID: 30071007
3. Mutational disruption of transcription factors binding and regulatory networks in a case of unexplained total fertilization failure.. *Journal of translational medicine*. PMID: 41188932
4. Upregulation of the transcription factor TFAP2D is associated with aggressive tumor phenotype in prostate cancer lacking the TMPRSS2:ERG fusion.. *Molecular medicine (Cambridge, Mass.)*. PMID: 32143573
5. Expression of Tfap2d, the gene encoding the transcription factor Ap-2 delta, during mouse embryogenesis.. *Gene expression patterns : GEP*. PMID: 12711551

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.4 |
| 高置信度残基 (pLDDT>90) 占比 | 31.9% |
| 置信残基 (pLDDT 70-90) 占比 | 13.3% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 50.7% |
| 有序区域 (pLDDT>70) 占比 | 45.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.4），有序残基占 45.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004979, IPR013854; Pfam: PF03299 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TFAP2A | 0.836 | 0.705 | — |
| TFAP2B | 0.795 | 0.611 | — |
| TFAP2C | 0.641 | 0.331 | — |
| KCTD1 | 0.599 | 0.137 | — |
| KCTD15 | 0.599 | 0.137 | — |
| CITED2 | 0.572 | 0.045 | — |
| EP300 | 0.562 | 0.099 | — |
| YEATS4 | 0.541 | 0.000 | — |
| CITED4 | 0.535 | 0.045 | — |
| CREBBP | 0.528 | 0.096 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| KRTAP12-3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP6-3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TNS2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP10-8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HOXD12 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| FAM168A | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KRTAP19-7 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TLE5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP10-7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.4 + PDB: 无 | pLDDT=62.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Golgi apparatus, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TFAP2D — Transcription factor AP-2-delta，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小452 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z6R9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000008197-TFAP2D/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TFAP2D
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z6R9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
