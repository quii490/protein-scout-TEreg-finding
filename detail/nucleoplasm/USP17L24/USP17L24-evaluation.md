---
type: protein-evaluation
gene: "USP17L24"
uniprot: "Q0WX57"
synonyms: ["USP17", "DUB3", "ubiquitin carboxyl-terminal hydrolase 17-like protein 24"]
date: 2026-06-28
tags: [protein-scout, nucleoplasm, nucleolus, deubiquitinase, histone-modification, te-regulation, evaluation, shortlisted]
status: shortlisted
---

## USP17L24 — 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | USP17L24 (亦称作 USP17, DUB3) |
| 蛋白全称 | Ubiquitin carboxyl-terminal hydrolase 17-like protein 24 |
| UniProt ID | Q0WX57 (U17LO_HUMAN, Swiss-Prot reviewed) |
| EC 编号 | 3.4.19.12 |
| 蛋白大小 | 530 aa; ~59.7 kDa |
| UniProt 证据等级 | 1: Evidence at protein level |
| UniProt 注释得分 | 5.0 / 5.0 |
| 亚细胞定位 | **Nucleus, nucleolus** (实验证据, PMID:17109758); Endoplasmic reticulum (序列相似性推断) |
| 染色体位置 | 4p16.1 (RS447 megasatellite 串联重复区) |
| Excel 分类 | Tier 2; HPA nuclear=False (与 UniProt 实验证据矛盾); PPI degree=3; Hotness=6 (中等热度) |
| HPA 注释 | "Uncertain" (抗体可能为阴性; 注意: HPA=False 不代表无核定位——USP17 家族核定位有独立实验验证) |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | 实验验证: Nucleus + nucleolus (PMID:17109758); HPA=False 与独立证据矛盾 |
| 蛋白大小 | 8/10 | ×1 | 8.0 | 530 aa, 59.7 kDa; 适合结构分析 |
| 新颖性 | 5/10 | ×5 | 25.0 | USP17 家族文献丰富 (~12+ 篇); 2025 Nature Comms 重大突破 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=67.69; USP 催化域 46.4% 高置信; C 端无序 |
| 调控结构域 | 8/10 | ×2 | 16.0 | USP 催化域 (80-375); 去泛素化酶 (EC 3.4.19.12); H2AK119ub1 底物 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=3; SUDS3 (HDAC 复合体), 多个核底物 (SET8, IL-33, ELK-1, c-Myc) |
| **加权总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位评估

**核定位为实验确证级别。** 虽然 HPA 在 Excel sheet 中标注为 "Nuclear=False" 及 "Uncertain" 可靠性，但独立实验证据提供更强的支持:

- **UniProt 瑞士-Prot 标注: "Nucleus, nucleolus"** (ECO:0000269, 实验证据, PMID:17109758)。该文献 (Shin et al., 2006, BMC Genomics) 对 USP17 家族蛋白进行了亚细胞定位实验。
- 与该条目关联的 `is_nuclear` 字段在 GraphTEBind 分类中被设为 **True** (基于实验证据)。
- HPA 的不一致可能源于: (1) USP17L24 在 RS447 megasatellite 中的拷贝数变异 (20-103 个拷贝/个体), 不同个体表达水平差异大; (2) HPA 抗体对该特定旁系同源物的检测灵敏度不足。
- Endoplasmic reticulum 定位是序列相似性推断 (ECO:0000250), 并非 USP17L24 的直接实验证据。

**核定位得分: 9/10** — 实验验证的 Nucleus + nucleolus 定位, 与 UniProt Swiss-Prot 标注一致。

#### 3.2 蛋白大小与序列特征

USP17L24 长度为 530 个氨基酸, 分子量约 59.7 kDa。蛋白结构由两部分组成:
- **N 端 USP 催化域 (80-375):** 硫醇蛋白酶折叠, 含催化三联体 (Cys89, His334)
- **C 端无序区 (477-530):** 可能参与蛋白-蛋白相互作用

等电点约 ~5.3 (酸性)。蛋白大小适中, 适合重组表达、晶体学和生化分析。

**蛋白大小得分: 8/10** — 530 aa 为理想的可操作尺寸。

#### 3.3 新颖性与文献覆盖

USP17 家族整体已有 **12+ 篇**主要研究文献 (加上综述), 但 USP17L24 单体蛋白的直接研究有限。这是因为 RS447 megasatellite 的多态性导致 **无法通过常规 RNAi 区分单个旁系同源物** (UniProt 明确标注: "RNAi probes are not isoform-specific")。大部分文献的 "USP17" 指代家族整体而非单个成员。

**关键文献里程碑:**

| 年份 | 里程碑 | PMID |
|---|---|---|
| 2000 | RS447 megasatellite 中发现 USP17 (奠基文献) | 10936051 |
| 2006 | USP17 家族亚细胞定位 (核仁定位确认) | 17109758 |
| 2011 | USP17 通过 K63 特异性去泛素化 SDS3 调控 HDAC 活性 | 21239494 |
| 2015 | USP17 调控 IL-33 稳定性与核功能 | 26610488 |
| 2019 | USP17 稳定 SET8, 抑制 p21 转录 (表观遗传调控) | 31533987 |
| 2021 | USP17 底物全景综述: 底物围绕细胞周期聚类 | 33227393 |
| 2025 | **USP17L 去泛素化 H2AK119ub1, 激活 2C 程序和 MERVL 逆转录转座子** | 40750602 |

2025 年 Nature Communications 论文是领域重大突破——首次建立 USP17 与组蛋白修饰和转座子激活的直接联系。

**新颖性得分: 5/10** — 家族研究丰富, 但单体区分度差。2025 年论文大幅提升了 TE 调控相关性。

#### 3.4 三维结构质量

AlphaFold 预测结构质量中等:

| pLDDT 区间 | 残基比例 |
|---|---|
| >90 (very high) | 46.4% |
| 70-90 (confident) | 11.9% |
| 50-70 (low) | 3.0% |
| <50 (very low) | 38.7% |

USP 催化域 (80-375) 为高置信折叠 — 46.4% 的高置信残基与催化域的 α/β 水解酶折叠一致。38.7% 的低置信残基几乎全部位于 C 端无序区 (382-412 和 477-530)。无 PDB 实验结构, 但 USP 家族的同源结构丰富, 可用于比较建模和药物设计。

**结构得分: 7/10** — 催化域折叠良好, C 端 IDR 可在后续优化中截短。

#### 3.5 调控结构域分析

**直接组蛋白去泛素化酶活性——这是 TE 调控的核心功能类别。**

| 结构域/特征 | 位置 | 功能 |
|---|---|---|
| USP 催化域 | 80-375 | 硫醇蛋白酶, K48/K63 链切割 |
| 催化 Cys (亲核) | Cys-89 | 去泛素化活性必须; C89S 完全失活 |
| 催化 His (质子受体) | His-334 | 催化三联体 |
| 无序区 1 | 382-412 | 碱性/酸性偏倚, 可能参与底物识别 |
| 无序区 2 | 477-530 | 极性/碱性偏倚, 可能参与 PPI |

**核内底物谱系 (实验验证):**

| 底物 | 底物类型 | USP17 功能 | 参考文献 |
|---|---|---|---|
| **H2AK119ub1** | 抑制性组蛋白标记 (PRC1) | 直接去泛素化, 去除沉默标记 | Lu 2025, Nat Comms |
| **SDS3 (SUDS3)** | Sin3A/HDAC 转录辅抑制因子 | K63 特异性去泛素化, 调控 HDAC 活性 | Ramakrishna 2011 |
| **SET8** | H4K20me1 甲基转移酶 | 稳定 SET8, 抑制 p21 转录 | Fukuura 2019 |
| **IL-33** | 核细胞因子/转录调控子 | K48/K63 去泛素化, 调控 IL13 | Ni 2015 |
| **ELK-1** | ETS 转录因子 | 去泛素化, 增强有丝分裂基因表达 | Ducker 2019 |
| **c-Myc** | 转录因子 | 稳定 c-Myc, 促进增殖/糖酵解 | Nagasaka 2022 |
| **ZSCAN4** | 2C 程序转录因子 | 去泛素化稳定, 防蛋白酶体降解 | Lu 2025 |

**调控结构域得分: 8/10** — 实验验证的组蛋白去泛素化酶 + 多个核转录底物。H2AK119ub1 去泛素化直接关联 TE 调控。

#### 3.6 PPI 网络

**PPI 网络以核调控为导向:**

| 互作伙伴 | 数据库 | 相关性 |
|---|---|---|
| UCHL1 | BioGRID | 另一种去泛素化酶 |
| SUDS3 (SDS3) | STRING (score 725) | Sin3A/HDAC 辅抑制复合体 → K63 去泛素化底物 |
| USP17L25, USP17L26 | STRING | 家族旁系同源物 |
| CT47A8 | STRING | 癌/睾丸抗原 |

**间接互作 (USP17 家族):** 小鼠正位同源物 (USP17LA) 的 BioGRID 数据包含 USP7 (SUMO 特异性去泛素化酶, 已知调控 PML 核体) 和 SUDS3。

**PPI 得分: 5/10** — 物理互作少 (degree=3), 但底物谱系远大于 PPI 数据, 反映了 DUB-底物关系不被 PPI 数据库充分覆盖。

#### 3.7 TE 调控相关性

**USP17L24 具有直接且机制明确的 TE 调控功能。**

| TE 调控维度 | 评估 |
|---|---|
| 直接 TE 结合 | 不确定 — 可能通过染色质间接作用 |
| 间接 TE 调控 | **强 — 直接去泛素化 H2AK119ub1 去沉默** |
| 组蛋白修饰 (TE 相关) | **确认 — H2AK119ub1 是 PRC1 抑制性标记的直接底物** |
| 2C 程序/TE 激活 | **确认 — 去沉默 MERVL 逆转录转座子和 MT2 元素** |
| 染色质重塑 | 通过 HDAC (SDS3) 间接调控 |

**2025 年关键发现 (Lu et al., Nature Communications):**
- USP17L 在胚胎干细胞中直接去泛素化 H2AK119ub1, 去除 PRC1 沉积的抑制性组蛋白标记
- **H2AK119ub1 在 Dux 位点的移除导致 2C 转录程序去抑制**
- 下游效应包括 **MERVL 逆转录转座子和 MT2 元素的转录激活**
- USP17L 敲低: MERVL/逆转录转座子转录降低, 多能性基因 (Nanog, Oct4) 升高, 端粒缩短, 染色体不稳定
- USP17L 是 **2 细胞胚胎基因激活程序的正面调控因子**

该机制非常类似于 ZGA (zygotic genome activation) 和胚胎发育背景下的已验证 TE 调控。USP17L24 作为该家族的成员, 极可能具有相同的生化活性。然而, 有重要注意事项: **当前无法区分该功能属于 USP17L24 单体, 还是属于其他 USP17 家族成员。**

#### 3.8 重要注意事项: RS447 Megasatellite 复杂性

USP17 基因座位于 RS447 megasatellite 串联重复中 (4p16.1), 拷贝数在不同个体间从 20 到 103 不等。高质量序列相似性导致:
- RNAi/CRISPR 探针无法区分旁系同源物
- 文献证据无法分配到特定 USP17L 成员
- UniProt 建议 "不能明确地将数据分配给特定 USP17 家族成员"

这意味着 USP17L24 评分中引用的生化功能是**家族级别的**, 而非特定于该单体。USP17L24 被选中的原因是其在核蛋白候选清单中的存在, 而非已知有独特功能——这反映了该基因座的实验局限性。

### 4. 总体评价

**67.2/100** | **Nucleoplasm + Nucleolus** | **SHORTLISTED**

**短列理由:**
1. **实验验证的核去泛素化酶** — 催化域完整, 在细胞核中活跃
2. **直接组蛋白底物** — H2AK119ub1 (PRC1 标记) 被直接去泛素化, 导致染色质去抑制
3. **TE 激活功能** — 2025 年关键论文建立了 USP17 → H2AK119ub1 → MERVL/MT2 转座子激活的完整机制
4. **丰富的核底物谱系** — 涉及 HDAC 辅抑制复合体 (SDS3)、组蛋白甲基转移酶 (SET8) 和转录因子 (IL-33, ELK-1, c-Myc, ZSCAN4)
5. **可操作的蛋白** — 530 aa, USP 催化域结构良好, 适合晶体学和小分子筛选

**弱点:**
1. USP17 家族冗余 — 无法区分旁系同源物, 所有功能为家族级
2. HPA 数据不一致 (HPA nuclear=False, 但 UniProt 实验数据为 Nucleus+nucleolus)
3. TE 调控方向为**激活** (去抑制 MERVL), 而非传统的 TE 沉默 — 这对 TE 沉默筛选项目可能适得其反
4. PPI 数据稀疏 (degree=3), 反映了 DUB-底物关系未被 PPI 数据库充分捕获
5. 无实验 3D 结构 (仅有同源模型)

**项目适配性:** 如果项目目标为 **TE 沉默因子筛选**, USP17L24 可能不是理想的候选者——它激活 TE 而非抑制。但如果项目接受 **染色质层面的 TE 调控蛋白** (包括双向调控), USP17L24 凭借 H2AK119ub1 去泛素化酶活性成为非常强的候选。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UCHL1 | BioGRID | 0 |

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q0WX57-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/USP17L24

### 5. 数据来源

| 数据库 | 访问内容 | 关键数据 |
|---|---|---|
| UniProt | Q0WX57 完整条目 | 序列, 结构域, 亚细胞定位, 催化活性, 注释得分 5.0 |
| AlphaFold DB | AF-Q0WX57-F1 | pLDDT=67.69, USP 域高置信折叠 |
| InterPro / Pfam | Q0WX57 结构域检索 | Peptidase C19, USP 域 (PF00443) |
| PubMed | "USP17" + "USP17L24" | ~12+ 篇文献, 关键论文 2025 Nat Comms |
| PMID: 40750602 | Lu et al. 2025, Nat Comms | USP17L → H2AK119ub1 → MERVL 激活 |
| PMID: 21239494 | Ramakrishna et al. 2011 | USP17 → SDS3 K63 去泛素化 |
| PMID: 31533987 | Fukuura et al. 2019 | USP17 → SET8 稳定 |
| PMID: 17109758 | Shin et al. 2006 | 核仁定位确认 |
| GraphTEBind PPI | grep USP17L24 / Q0WX57 | BioGRID + STRING 互作 |
| GraphTEBind 分类 | nuclear_proteins_master.tsv | Tier 2, is_nuclear=True, is_deubiquitinase=True |
