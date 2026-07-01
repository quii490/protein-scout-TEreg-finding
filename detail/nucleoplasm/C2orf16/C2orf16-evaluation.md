---
type: protein-evaluation
gene: "C2orf16"
uniprot: "Q68DN1"
synonyms: ["SPATA31H1", "FAM75A-like"]
date: 2026-06-28
tags: [protein-scout, nucleoplasm, nuclear-bodies, evaluation, rejected]
status: rejected
---

## C2orf16 / SPATA31H1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SPATA31H1 (旧名 C2orf16) |
| 蛋白全称 | Spermatogenesis-associated protein 31H1 |
| UniProt ID | Q68DN1 (S31H1_HUMAN, Swiss-Prot reviewed) |
| 蛋白大小 | 1,984 aa; ~224.3 kDa |
| UniProt 证据等级 | 1: Evidence at protein level |
| UniProt 注释得分 | 4.0 / 5.0 |
| 亚细胞定位 | Nucleoplasm; Nuclear bodies; Cytosol (HPA: Uncertain reliability) |
| 染色体位置 | 2p23.3 |
| Pharos 开发等级 | Tdark (极度未知) |
| Excel 分类 | Tier 3; HPA nuclear=True; PPI degree=6; Hotness=0 (冷门) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | HPA: Nucleoplasm+Nuclear bodies+Cytosol, Uncertain; GO-CC HDA only |
| 蛋白大小 | 0/10 | ×1 | 0.0 | 1,984 aa — 超大蛋白 (~224 kDa)，含 342 aa 串联重复区 |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed~8 篇总文献，仅 2 篇直接研究; Pharos Tdark |
| 三维结构 | 0/10 | ×3 | 0.0 | pLDDT=34.94; 93.6% 残基 pLDDT<50; 无折叠结构域 |
| 调控结构域 | 0/10 | ×2 | 0.0 | 无 Pfam/InterPro 结构域; 无 DNA 结合域; 无酶活性域 |
| PPI | 2/10 | ×3 | 6.0 | PPI degree=6 (BioGRID: NCL, PRC1, DDX39A, ZRANB1 + STRING ~15) |
| **加权总分** | | | **67.0/180** | |
| **归一化总分** | | | **37.2/100** | |

### 3. 详细分析

#### 3.1 核定位评估

**核定位证据质量低。** HPA 免疫荧光检测到 Nucleoplasm + Nuclear bodies + Cytosol 的三重定位模式，但两个抗体 (HPA052136, HPA056962) 均被标记为 "Uncertain" 可靠性。Gene Ontology 核定位注释 (GO:0005634) 仅来源于高通量直接测定 (HDA, PMID:21630459)，无低通量实验验证。Bekpen et al. (2017) 对 SPATA31 基因家族的细胞学研究表明其定位于**核仁**，UV 照射后重新分布至全核——但这些实验针对的是染色体 9 上的 SPATA31 拷贝，并不能直接外推到染色体 2 上的 SPATA31H1。

GO 条目同时包括 extracellular exosome (GO:0070062, HDA)、extracellular space (GO:0005615, HDA) 和 vesicle (GO:0031982, HDA)，均为高通量证据。**不支持明确的核驻留功能。**

**核定位得分: 4/10** — HPA Uncertain + 无低通量验证 + 胞质/外泌体混杂定位。

#### 3.2 蛋白大小与序列特征

SPATA31H1 长度为 **1,984 个氨基酸**，分子量约 224 kDa，在所有人类蛋白中属于特大型。蛋白质的 C 端 ~342 个残基 (1593-1935) 由 **27 个 P-S-E-R-S-H-H-S 基序的串联重复**构成。UniProt 注释称该重复区 "形成反平行 β-结构"，但在 AlphaFold 中该区域完全无序。

**序列组成:**
- 高度碱性 (pI ~10.09)
- 极端富含丝氨酸和组氨酸 (重复区)
- 20 个组成偏倚区域 (polar residues, basic residues, low-complexity)

**蛋白大小得分: 0/10** — 1,984 aa 过大，不适合常规结构生物学和生化分析。

#### 3.3 新颖性与文献覆盖

**极度冷门。** PubMed 检索 "C2orf16 OR SPATA31H1" 仅返回 8 篇文献。其中仅 2 篇直接聚焦该蛋白:
1. Wang W et al. (2026, BMC Oral Health) — SPATA31H1 罕见错义变异与遗传性牙龈纤维瘤病
2. Greither T et al. (2023, Andrology) — 人类精子蛋白质组 panel

其余 6 篇为 GWAS/组学关联研究 (NAFLD-MASLD, 代谢综合征, 心血管疾病, BCAA 水平, IBS-NAFLD, 家族性低β脂蛋白血症)，SPATA31H1 仅作为关联位点出现。**Pharos 分类为 Tdark**，代表开发等级最低、最未知的蛋白类别。

SPATA31 基因家族整体比单体蛋白更受关注: Bekpen et al. (2017, BMC Genomics, PMID:28264649) 发现该家族在类人猿中经历强烈正向选择，在人类中经历了大量片段重复 (二倍体基因组平均 7.5 个拷贝)，且灵长类拷贝获得了隐花色素/光裂合酶结构域和 PCNA 互作结构域——但这些功能结构域**不存在于 SPATA31H1**。

**新颖性得分: 9/10** — 文献极少，但高新颖性在此情境中为负面信号 (缺乏功能表征)。

#### 3.4 三维结构质量

**结构预测极差。** AlphaFold 预测:
| pLDDT 区间 | 残基比例 |
|---|---|
| >90 (very high) | 0.0% |
| 70-90 (confident) | 1.6% |
| 50-70 (low) | 4.8% |
| <50 (very low) | **93.6%** |

**SPATA31H1 是近乎完全的内在无序蛋白 (IDP)。** 序列中不存在任何可识别的折叠结构域:
- 无 Pfam 结构域 (Pfam 数据库中无条目)
- 无 InterPro 功能结构域 (PANTHER PTHR33888 除外，为未表征的 RIKEN cDNA 条目)
- UniProt 标注 5 个大型无序区，其中最长的 C 端区域跨越残基 1439-1984 (546 个残基)
- 无信号肽、无跨膜螺旋、无酶活性位点

作为 IDP，SPATA31H1 可能通过与结合伙伴相互作用后折叠，或以前折叠状态存在。这与 Bekpen et al. 提出的支架/调控蛋白功能假说一致，但缺乏直接实验证据。

**结构得分: 0/10** — 93.6% 无序，无可鉴定折叠结构域。

#### 3.5 调控结构域分析

**无任何已知调控结构域。**
- DNA 结合域: 无 (无 bZIP, bHLH, zf-C2H2, homeobox, AT-hook, HMG-box 等)
- 染色质结合域: 无 (无 bromodomain, chromodomain, PHD finger, PWWP, MBT 等)
- 组蛋白修饰域: 无 (无 SET, MYND, DOT1, JmjC 等)
- 酶活性域: 无
- 蛋白相互作用结构域: 无 (无 SH2, SH3, WW, PDZ, WD40 等标注)
- 唯一的序列特征: P-S-E-R-S-H-H-S 串联重复区 (功能未知)

**调控结构域得分: 0/10** — 不存在任何已知调控结构域。P-S-E-R-S-H-H-S 重复区可能参与蛋白互作或 RNA 结合，但无任何实验证据。

#### 3.6 PPI 网络

**PPI 网络小而杂。** BioGRID 物理相互作用:
| 互作伙伴 | 功能 | 证据 |
|---|---|---|
| NCL (Nucleolin) | 核仁蛋白, rRNA 转录/加工 | 物理互作 (Jiao 2024) |
| PRC1 | 细胞分裂调控 | 物理互作 (Capalbo 2019) |
| DDX39A | DEAD-box RNA 解旋酶 | 物理互作 (Shi 2020) |
| ZRANB1 | 去泛素化酶, DNA 损伤应答 | 物理互作 (Chen 2022) |

STRING 扩展网络 (~15 个互作伙伴) 包括核糖体蛋白 (RPL23, MRPL21/43/46)、转录相关因子 (GTF3C2, NRBP1)、和锌指蛋白 (ZNF512, ZSWIM9)。GraphTEBind 预测模型给出 PRR30 的高置信度互作 (score=0.531)。

NCL (核仁素) 互作与核仁定位一致，但其他互作伙伴功能分散，缺乏指向特定通路的网络聚集。

**PPI 得分: 2/10** — 互作伙伴少 (degree=4 物理互作)，无通路富集，功能信息有限。

#### 3.7 TE 调控相关性

**无任何 TE 调控证据。**

| TE 调控维度 | 评估 |
|---|---|
| 直接 TE 结合 | 无证据 — 无 DNA 结合域 |
| 间接 TE 调控通路 | 无证据 — 无染色质/表观遗传功能域 |
| 生殖细胞特异性表达 | 是 (睾丸富集, 早期精细胞 476.0 TPM) |
| 转座子表达调控 | 无证据 |
| piRNA 通路 | 无关联 |
| 染色质重塑 | 无证据 |

SPATA31H1 的睾丸/精子特异性表达是唯一可能与生殖细胞 TE 沉默间接关联的属性。但该蛋白不含任何可支持染色质调控、转录调控或表观遗传修饰的功能结构域。作为高度无序蛋白，其可能的功能模式 (支架、相分离、信号整合) 均与 TE 调控无直接联系。

染色体 9 上的 SPATA31 家族成员在 UV 响应和 DNA 损伤修复中有功能 (Bekpen 2017)，但该表型与 TE 调控的关联性极弱。

### 4. 总体评价

**37.2/100** | **Nucleoplasm (Uncertain)** | **REJECTED**

**拒绝理由:**
1. **蛋白过大 (1,984 aa, 224 kDa)** — 不适合系统生化分析
2. **93.6% 无序** — 近乎完全的内在无序蛋白，缺乏可操作的结构域
3. **无功能注释** — 无 Pfam/InterPro 结构域, 无分子功能, 无通路归属
4. **无 TE 调控相关性** — 不含 DNA 结合域, 染色质结构域, 或表观遗传修饰域
5. **核定位证据不可靠** — HPA Uncertain, 胞质/外泌体混杂定位
6. **文献极度匮乏** — PubMed 仅 8 篇, 2 篇直接相关
7. **Tdark** — Pharos 最低开发等级

SPATA31H1 是一个有趣的进化生物学研究对象 (灵长类特异性扩增、强烈正向选择)，但完全不适合 TE 调控蛋白筛选。其巨型体积、极度无序和零功能表征使其无法在候选蛋白 pipeline 中产生价值。

### 5. 数据来源

| 数据库 | 访问内容 | 关键数据 |
|---|---|---|
| UniProt | Q68DN1 完整条目 | 序列, 定位, 无序区, 变异 |
| AlphaFold DB | AF-Q68DN1-F1 | pLDDT 分布, 预测结构 |
| InterPro / Pfam | Q68DN1 结构域检索 | 无结构域 (Pfam 无条目) |
| PubMed | "C2orf16 OR SPATA31H1" | 8 篇文献 |
| HPA | SPATA31H1 | 组织表达, 亚细胞定位 |
| GraphTEBind PPI | grep SPATA31H1 / C2orf16 / Q68DN1 | BioGRID + STRING 互作 |
| Pharos / TCRD | SPATA31H1 | Tdark 分类 |
| Bekpen et al. 2017 | SPATA31 基因家族 | 进化, 片段重复, UV 响应 |
